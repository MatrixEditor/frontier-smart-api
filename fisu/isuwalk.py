import re

from fisu import (
  to_ui24,
  to_ui16,
  to_ui32,
  skip,
  verify_skip
)

MAGIC_HEADER = [
  0x76, 0x11, 0x00, 0x00, # ISU Signature
  # 0x7c, 0x00, 0x00, 0x00, File-Header length = 124
  # 0x01, 0x00, 0x00, 0x00  MeOS Version -> (01 00) => MajorVersion, (00 00) => MinorVersion
]

ISU_HEADER_LEN = 0x7c

ISU_CORE_OFFSET = 22828
ISU_FSH1_DA_00BLOCK_SIZE = 5308
ISU_FIELD_DEF_OFFSET = 2768

ISU_SYS_ENTRY_INDICATOR  = [0x05, 0x00, 0x10, 0x00]
ISU_SYS_ENTRY_10_PATTERN = [0x06, 0x02, 0x1F, 0x2B]
ISU_SYS_ENTRY_20_PATTERN = [0x0A, 0x02, 0x7E, 0xDB]
ISU_BUF_SIZE_INDICATOR   = [0x20, 0x00, 0x00, 0x53]

class FshElement:
  def __init__(self, root, tag: str, attributes: dict, text: str = None) -> None:
    self.tag = tag
    self.attr = attributes
    self.root = root
    self.text = text
    self.elements = []

  def get_elements(self) -> list:
    return self.elements

  def get_element(self, tag):
    for elem in self.elements:
      if elem.tag == tag:
        return elem

  def set_attribute(self, name, value):
    if name: self.attr[name] = value

  def get_attribute(self, name):
    if name: return self.attr[name]

  def toXml(self, indent='') -> str:
    txt = self.text if self.text else ""
    xml_str = "%s<%s%s" % (
      indent, self.tag,
      self._attr_to_str()
    )
    if not self.text and len(self.elements) == 0:
      return xml_str + "/>"
    else:
      xml_str += '>'
      if len(self.elements) != 0:
        for element in self.elements:
          xml_str += '\n' + element.toXml(indent=indent + '\t')
      if self.text:
        return xml_str + "%s</%s>" % (txt, self.tag)
      else: 
        return xml_str + "\n%s</%s>" % (indent, self.tag)

  def _attr_to_str(self) -> str:
    if len(self.attr) == 0: 
      return ""
    else:
      x_str = []
      for key in self.attr:
        value = self.attr[key]
        if type(value) == str:
          x_str.append('%s="%s"' % (key, value))
        else:
          x_str.append('%s=%d' % (key, value))
      return ' ' + ', '.join(x_str)
    
  def append(self, e):
    if e: self.get_elements().append(e)
  
  def rem_attribute(self, name):
    if name: self.attr.pop(name)

class FshTree(FshElement):
  def __init__(self, root: FshElement = None, attributes: dict = None) -> None:
    super().__init__(root, 'fsh1', 
      attributes if attributes else {'name': 'Frontier-Silicon-FS'}
    )

def _parse_file(root: FshElement, index, start, offset, buffer, level=0, verbose=False) -> tuple:
  name_len = buffer[index]
  index += 1
  offset += 1

  try:
    name = 'root' if name_len == 0 else str(buffer[index:index+name_len], 'utf-8')
    index += name_len
    offset += name_len
  except Exception as e:
    if verbose: print("[-] Could not read filename: %s" % e)
    name = '<>'

  file_size = to_ui32(buffer, index)
  file_offset = to_ui32(buffer, index+4)
  file_compression = to_ui32(buffer, index+8)
  
  index += 12
  offset += 12
  
  entry = FshElement(root, 'file', {
    'type': 0x00,
    'name': name,
    'size': file_size,
    'offset': file_offset,
    'compressed': 'True' if file_compression != file_size else "False",
    'compression_size': file_compression,
    'real_offset': start + file_offset
  })
  root.append(entry)
  if verbose: 
    print("%s- %s type=0x00(file), offset=%d, compressed=%s, comp_size=%d" % (
      '|  '*level, name, file_offset, 
      "False" if file_compression == file_size else "True",
      file_compression
    ))
  return (index, offset)

def isu_parse_entry(root: FshElement, index, start, offset, buffer, level = 0, verbose=False):
  entry_type = buffer[index]
  index += 1
  if entry_type == 0x00:
    return _parse_file(root, index, start, offset, buffer, level, verbose)
  elif entry_type == 0x01:
    return _parse_dir(root, index, start, offset, buffer, level, verbose)
  else:
    if verbose: print("[-] Invalid entry type: %#x" % entry_type)

def _parse_dir(root: FshElement, index, start, offset_index, buffer, level=0, verbose=False) -> tuple:
  name_len = buffer[index]
  index += 1
  offset_index += 1

  try:
    name = 'root' if name_len == 0 else str(buffer[index:index+name_len], 'utf-8')
  except Exception as e:
    if verbose: print("[-] Could not read filename: %s" % e)
    name = '<>'
  
  entries = buffer[index+name_len]
  index += 1 + name_len
  offset_index += 1 + name_len
  directory = FshElement(root, 'dir', {
    'name': name,
    'type': 0x01,
    'entries': entries,
  })
  if verbose: print('%s| %s/ (entries=%d)' % ('|  '*level, name, entries))
  for _ in range(entries):
    index, offset_index = isu_parse_entry(directory, index, start, offset_index, buffer, level + 1, verbose)
  root.append(directory)
  return (index, offset_index)

def isu_parse_header_name(root: FshElement, buffer: bytes, entry_name: str,
               index: int, verbose: bool = False) -> tuple:
  endpos = buffer.index(b" ", index)
  name = str(buffer[index:endpos], 'utf-8')
  
  index = endpos
  while buffer[index] == 0x20:
    index += 1
  
  if root: root.append(FshElement(root, entry_name, text=name, attributes={}))
  if verbose: print("  - %s: '%s'" % (entry_name, name))
  return (index, name)

def isu_parse_table_entry(root: FshElement, buffer: bytes, 
                          index: int, verbose: bool = False,
                          entry_num: int = 0) -> tuple:
  failure = (index, False, None)
  # Indicator check:
  index, success = skip(buffer, index, ISU_SYS_ENTRY_INDICATOR)
  if not success:
    if verbose: print("[-] Malformed sys-entry: signature not found")
    return failure

  # Entry number
  entry_initial_value = buffer[index]
  entry_number = (entry_initial_value & 0xf0) >> 4
  index += 1
  ptn = []
  if entry_number == entry_num + 1:
    entry_type = entry_number
    ptn.append(0xA8)
  else:
    entry_type = 0xf
    ptn.append(0xB8)
  
  ptn += [0x0A, 0x00, 0x00, 0xB0 | entry_num*4, 0x0A, 0x00]
  index, success = verify_skip(
    skip(buffer, index, ptn), 
    "[-] Malformed sys-entry: could not skip pattern", 
    verbose
  )
  if not success: return failure

  entry_u2 = 0
  if entry_number == 1:
    index, success = verify_skip(
      skip(buffer, index, ISU_SYS_ENTRY_10_PATTERN), 
      "[-] Malformed sys-entry: could not skip 10-pattern", 
      verbose
    )
    if not success: return failure
  elif entry_number == 2:
    index, success = verify_skip(
      skip(buffer, index, ISU_SYS_ENTRY_20_PATTERN), 
      "[-] Malformed sys-entry: could not skip 20-pattern", 
      verbose
    )
    if not success: return failure
  else:
    entry_crc = buffer[index]
    if entry_crc != entry_initial_value - 2:
      if verbose: print("[-] Malformed sys-entry: could not verify entry")
      return index, False
    
    entry_u2 = to_ui16(buffer, index+2)
    index += 4
  
  e = FshElement(root, 'entry', attributes={
      'type': entry_type,
      'partition': entry_number,
      'unknown': entry_u2
    })
  if root: root.append(e)
  return index, True, e

def isu_parse_buf_or_size(root: FshElement, buffer: bytes, index: int,
                          verbose: bool = False) -> tuple:
  failure = (index, False)
  
  index, success = verify_skip(
    skip(buffer, index, ISU_BUF_SIZE_INDICATOR),
    "[-] Malformed indicator for buffer or size",
    verbose
  )
  if not success: return failure

  name_len = buffer[index]
  index += 1
  index, success = verify_skip(
    skip(buffer, index, [0x00, 0x04, 0x00]),
    "[-] Malformed byte code: expected 00 04 00",
    verbose
  )
  if not success: return failure

  try:
    # NOTE: name_len - 1 because name string is \0 terminated
    name = str(buffer[index:index+name_len - 1], 'utf-8')
    index += name_len
  except Exception as e:
    if verbose: print("[!] Exception: %s" % e)
    return failure

  data_size = 24 - name_len
  if data_size - 8 < 0:
    if verbose: print("[-] Malformed byte code: data size has to be > 8bytes")
    return failure
  
  index += data_size - 8
  size = to_ui32(buffer, index) # maybe to_ui24()
  index += 8

  if root: 
    root.append(FshElement(root, name, attributes={
      'Size' if 'Size' in name else 'Buffer': size
    }))
  if verbose: print("  - %s: %s=%d" % (name, 'Size' if 'Size' in name else 'Buffer', size))
  return index, True

def isu_list_fields(root: FshElement, buffer: bytes, verbose=False):
  field_root = FshElement(root, 'fieldlist', {})
  if root: root.append(field_root)
  index = ISU_FIELD_DEF_OFFSET # offset for DecompBuffer
  while True:
    index, success = isu_parse_buf_or_size(field_root, buffer, index, verbose)
    if not success: exit(0)
    if buffer[index] != 0x20:
      break
  return field_root.get_elements()

ISU_CORE_SIGNATURE = [0x1B, 0x00]

# << unidentified >>
ISU_UI_SECTION_INDICATOR = (
  (0x05, 0x80),
  (0x05, 0x80),
  (0x05, 0x80),
  (0x04, 0x00)
)
def isu_ui_parse_section(section: int, buffer: bytes, index: int = 0x28c,
                         root: FshElement = None, verbose=False):#  -> tuple[int, list[bytes]]
  result = (index, None)
  if section > 4 or section < 1:
    if verbose: print('[-] Invalid section number:', section)
    return result 

  # skip trailing 0x00 bytes
  while buffer[index] == 0x00: index += 1
  
  if section == 4:
    index, success = verify_skip(
      skip(buffer, index, (0x04, 0x00)),
      '[-] Failed to skip indicator of section-4: 0x0400',
      verbose
    )
  else:
    index, success = verify_skip(
      skip(buffer, index, (0x50, 0x80)),
      '[-] Failed to skip indicator of section-%d: 0x5080' % section,
      verbose
    )
  
  if not success: return result

  block_size = to_ui16(buffer, index)
  index += 2
  data_blocks = []
  attr = {'id': section, 'size': block_size}

  if verbose: print('[-] Section-%d: size=%d' % (section, block_size))
  if section == 1:
    attr['blockCount'] = block_size // 12
    if verbose: print(' '*4, '- BlockCount:', attr['blockCount'])

    for i in range(1, attr['blockCount']):
      data_blocks.append(buffer[index+((i-1)*12):index+(i*12)])
  elif section == 2:
    pass

  if root: root.append(FshElement(root, 'section', attr))
  return (index, data_blocks)

