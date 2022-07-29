import argparse
import re
import os
import subprocess

from time import sleep

from . import (
  isuwalk,
  sigtable,
  fsversion
)

__BANNER__ = """
\t\tISU-Inspector Tool
---------------------------------------------------------------------
"""

RE_ISU_SUFFIX = r".*isu.*"
RE_FSH_PATTERN = br"FSH1"

EXTRACT_HEADER = 0xff0
EXTRACT_ARCHIVE = 0xff1
EXTRACT_CORE   = 0xff2

def parse_header(root: isuwalk.FshElement, buffer: bytes, 
                 sig_table: dict,
                 verbose: bool = False) -> tuple:
  index = 0

  if verbose: print("[+] Analyzing ISU File header...")
  sleep(1)
  while True:
    if index == 4:
      break

    if buffer[index] != isuwalk.MAGIC_HEADER[index]:
      if verbose: print("[-] Unknown file type: magic header not recognized")
      return -1
    index += 1
  
  header_len = isuwalk.to_ui32(buffer, index)
  if header_len != isuwalk.ISU_HEADER_LEN:
    print("[-] Unknown header size: %d" % header_len)
  
  print("  - MeOS Version: %d" % (isuwalk.to_ui32(buffer, index+4)))
  index += 8

  fsv = fsversion.FSVersion()
  fct = fsversion.FSCutomization()

  index, version = isuwalk.isu_parse_header_name(root, buffer, 'Version', index, verbose)
  fsv.loads(version)
  if verbose:
    print("     | SDK Version: %s" % (fsv.sdk_version))
    print("     | Revision: %s" % (fsv.revision))
    print("     | Branch: %s\n" % (fsv.branch))
    
  index, custom = isuwalk.isu_parse_header_name(root, buffer, 'Customisation', index, verbose)
  fct.loads(custom)
  if verbose:  
    print("     | DeviceType: %s" % ('internet radio' if fct.device_type == 'ir' else fct.device_type))
    print("     | Interface: %s" % ('multi media interface' if fct.interface == 'mmi' else fct.interface))
    print("     | Module: %s (version=%s)\n" % (fct.get_module_name(), fct.module_version))
  
  if sig_table and 'filesigs' in sig_table:
    sleep(1)
    if root: sig_list = isuwalk.FshElement(root, 'list', {})
    count = 0
    for signature in sig_table['filesigs']:
      bt_header = bytes(
        [int(x, 16) for x in signature['Header'].split(' ')]
      )
      try:
        match = re.search(bt_header, buffer)
        if match:
          count += 1
          if root: sig_list.append(isuwalk.FshElement(
            sig_list, 'signature', attributes={
                'span': match.span().__str__(),
                'header': signature['Header'],
                'extensions': signature['FileExtensions']
              }
            )
          )
      except: continue
    if verbose: print('  - Signature(s) detected: count="%s"\n' % count)
    if root: root.append(sig_list)

  properties = buffer[index:isuwalk.ISU_HEADER_LEN]
  index = header_len
  
  print("[+] SystemEntries:")
  sleep(1)
  entry_root = isuwalk.FshElement(root, 'entrylist', {})
  if root: root.append(entry_root)

  count = 0
  while True:
    # TODO: fix errors
    index, success, element = isuwalk.isu_parse_table_entry(entry_root, buffer, index, verbose, count)
    if not success: exit(0)
    count += 1
    
    if verbose:
      _t = element.get_attribute('type')
      e_type = 'FS' if _t < 0xa else 'END'
      print("  - SysEntry: type=%s, " % e_type, end='')
      if e_type == 'FS':
        print('partition=%d' % _t, end='')
        if _t == 2: print(' (Could be DirectoryArchive for Web-Data)')
        else: print()
      else:
        print('magicnumber=%#x\n' % element.get_attribute('unknown'))
    if buffer[index] == 0x00: break

  print("[+] Declared Fields:")
  sleep(1)
  isuwalk.isu_list_fields(entry_root, buffer, verbose)
  print()
  return (index, fsv, fct)

def parse_directory_archive(root: isuwalk.FshElement, buffer: bytes, verbose: bool = False) -> int:
  for match in re.finditer(RE_FSH_PATTERN, buffer):
    pos = match.end()
  
  if not pos:
    if verbose: print("[-] Directory archive not found")
  
  fsh = "FSH1"
  index = pos
  size = isuwalk.to_ui32(buffer, index)
  if verbose: print("[+] Found a directory archive(size=%d bytes, name='FSH1')" % size)

  index += 4
  isuwalk.to_ui16(buffer, index)
  
  index += 2
  index_len = isuwalk.to_ui32(buffer, index)
  if verbose: print("[+] Reading Index(size=%d bytes, offset=%d)...\n" % (index_len, index))
  sleep(1)

  index += 4
  tree = isuwalk.FshTree(root, attributes={
    'name': fsh + ' Frontier Silicon Filesystem v1',
    'index_size': index_len,
    'archive_size': size,
    'offset': pos + 6
  })
  index, _ = isuwalk.isu_parse_entry(tree, index, pos, 0, buffer, verbose=verbose)
  
  if verbose: print("\n[+] Successfully parsed the Index-Header\n")
  if root: root.append(tree)

def save_entry(root: isuwalk.FshElement, buffer: bytes, path: str, verbose: bool = False):
  name = root.get_attribute('name')
  if root.get_attribute('type') == 0x00:
    # subprocess.run("dd if=%s of=%s bs=1 skip=%d count=%d") only unix
    with open(path + name, 'wb') as _res:
      off = root.get_attribute('offset')
      if root.get_attribute('compressed') == 'True':
        _res.write(buffer[off:off+root.get_attribute('compression_size')])
      else:
        _res.write(buffer[off:off+root.get_attribute('size')])
  else:
    if name == 'root':
      name = 'fsh1'
    os.mkdir(path + name)
    for element in root.get_elements():
      save_entry(element, buffer, path + name + '/', verbose)

def extract_bytes(root: isuwalk.FshElement, buffer: bytes, e_type: int, verbose: bool = False):
  path = root.get_attribute('path').split('/')[-1][:-8]
  try:
    if e_type == EXTRACT_HEADER:
      with open(path + '.header.bin', 'wb') as _res:
        _res.write(buffer[:isuwalk.ISU_HEADER_LEN])
    elif e_type == EXTRACT_ARCHIVE:
      fsh = root.get_element('fsh1')
      if not fsh:
        if verbose: print("[-] Failed to read FSH1: add --archive to include parsing the archive.")
        exit(0)
      
      path = '_archive.extracted'
      os.mkdir(path)
      buffer = buffer[fsh.get_attribute('offset'):]
      for element in fsh.get_elements():
        save_entry(element, buffer, path + '/', verbose)
    elif e_type == EXTRACT_CORE:
      fields: list = root.get_element('fieldlist')
      if not fields:
        fields: list = isuwalk.isu_list_fields(None, buffer, verbose)

      copy_size = -1
      for field in fields:
        if field.tag == 'CompSize':
          copy_size = field.get_attribute('Size')
          break
      
      if copy_size == -1:
        if verbose: print("[-] Invalid input file: CompSize not found")
        exit(0)
      
      with open(path + '.core.bin', 'wb') as _res:
        _res.write(buffer[isuwalk.ISU_CORE_OFFSET:isuwalk.ISU_CORE_OFFSET+copy_size])
    else:
      if verbose: print("[-] Invalid extraction option")
    
    if verbose: print("\n[+] Saved extracted output successfully")
  except OSError as e:
    if verbose: print("[-] Failed to open resource: %s" % e)
    exit(0)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-if', type=str, required=True, 
    help="The input file (must have the *.isu.* extension)"
  )
  parser.add_argument('-of', type=str, required=False,
    help="The output file (Format: XML)."
  )
  parser.add_argument('--verbose', action='store_true', default=False,
    help="Prints useful information during the specified process."  
  )

  group_info = parser.add_argument_group("information gathering")
  group_info.add_argument('--header', action='store_true', default=False, 
    help="Parses the header of the given file and extracts information."
  )
  group_info.add_argument('--archive', action='store_true', default=False, 
    help="Parses the virtual filesystem."
  )
  group_info.add_argument('--sig', type=str, default=None, 
    help="The path to the 'file_sigs.json file'. This option includes the signature search."
  )
  
  group_extract = parser.add_argument_group("extract data")
  group_extract.add_argument('-e', '--extract', action='store_true', default=False,
    help="Extract data (usually combined with other parameters)."
  )
  group_extract.add_argument('--core', action='store_true', default=False,
    help="Extract the compressed core partition source."
  )

  nspace = parser.parse_args().__dict__
  # nspace = {
  #  'if': 'ir-mmi-FS2026-0500-0549_V2.12.25c.EX72088-1A12.isu.bin' ,
  #  'verbose': True ,
  #  'header': False,
  #  'archive': False,
  #  'extract': True,
  #  'core': True
  # }
  verbose = nspace['verbose']

  if verbose: print(__BANNER__)
  if "if" not in nspace:
    print("[-] Input file has to be specified!")
    exit(0)
  else:
    _path = nspace['if']

  _opath = nspace['of'] if "of" in nspace else None
  root = isuwalk.FshElement(None, 'isu', {'path': _path})
  sigs = sigtable.load_file_signatures(nspace['sig']) if "sig" in nspace else None 

  if not re.match(RE_ISU_SUFFIX, _path) and not nspace['header']:
    print("[-] The input file must have the *.isu.* extension")
    exit(0)

  try:
      with open(_path, 'rb') as _file:
        buffer = _file.read()
        if nspace['header']:
          index, fsv, fct = parse_header(root, buffer, sigs, verbose)
          if nspace['archive']:
            if not fct: 
              print("[!] Fatal error: FSCustomisation should not be None")
              exit(-1)
            if not fct.interface: fct.interface = fct.repr.split('-')[1]
            if fct.interface != 'mmi':
              if verbose: print(
                "[-] Warning: Could not handle isu.bin file > Interface not supported"
              )
              exit(-1)
            
        # TODO: check if file is of type mmi
        if nspace['archive']:
          parse_directory_archive(root, buffer, verbose)

      if _opath and root:
        with open(_opath, 'w') as _output:
          _output.write('<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>\n')
          _output.write(root.toXml())
        
        if verbose: print("[+] Saved output to %s" % _opath)

      if nspace['extract']:
        if nspace['header']: extract_bytes(root, buffer, EXTRACT_HEADER, verbose)
        if nspace['archive']: extract_bytes(root, buffer, EXTRACT_ARCHIVE, verbose)
        if nspace['core']: extract_bytes(root, buffer, EXTRACT_CORE, verbose)
  except OSError:
    print("[-] Unable to open the input file!")

  
  
