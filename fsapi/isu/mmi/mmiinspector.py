# MIT License

# Copyright (c) 2022 MatrixEditor

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import re

from fsapi.isu.fsfs import FSFSFile

from .. import (
  ISUInspector, 
  ISUFile, 
  ISUCompressionField,
  ISUHeader, 
  ISU_MAGIC_BYTES,
  FSCutomisation,
  FSVersion,
  FSFSTree,
  SetInspector
)

from ..ioutils import *

__all__ = [
  'MMIInspector', 'MMI_HEADER_LENGTH'
]

MMI_HEADER_LENGTH = 124
MMI_BUF_SIZE_INDICATOR   = [0x20, 0x00, 0x00, 0x53]

@SetInspector("mmi")
class MMIInspector(ISUInspector):

  def get_header(self, buffer: ISUFile, offset: int = 0, **kwgs) -> ISUHeader:
    verbose = 'verbose' in kwgs and kwgs['verbose']

    index, success = verify_skip(
      skip(buffer._file, offset, ISU_MAGIC_BYTES),
      "Malformed ISU-File",
      verbose
    )

    if not success: return None
    if verbose: print("[+] Analyzing ISU File header...")

    header = ISUHeader()
    header._size = to_ui32(buffer, index)

    if header.size != MMI_HEADER_LENGTH:
      if verbose: print("[-] Unknown header size: %d" % header.size)
      return header
    
    index += 4
    header.meos_version = to_ui32(buffer, index)
    if verbose:
      print("  - MeOS Version: %d" % (header.meos_version))

    fsv = FSVersion()
    fsc = FSCutomisation()

    index += 4
    index, fsv_name = self._get_header_name(buffer, index)
    index, fsc_name = self._get_header_name(buffer, index)

    fsv.loads(fsv_name)
    fsc.loads(fsc_name)
    if verbose:
        print("  - Version: '%s'" % str(fsv))
        print("     | SDK Version: %s" % (fsv.sdk_version))
        print("     | Revision: %s" % (fsv.revision))
        print("     | Branch: %s\n" % (fsv.branch))
        print("\n  - Customisation: '%s'" % str(fsc))
        print("     | DeviceType: %s" % ('internet radio' if fsc.device_type == 'ir' else fsc.device_type))
        print("     | Interface: %s" % ('multi media interface' if fsc.interface == 'mmi' else fsc.interface))
        print("     | Module: %s (version=%s)\n" % (fsc.get_module_name(), fsc.module_version))

    header._customisation = fsc
    header._version = fsv

    return header

  def _get_header_name(self, buffer: ISUFile, index: int) -> tuple:
    endpos = buffer._file.index(b" ", index)
    fsv_name = str(buffer[index:endpos], 'utf-8')
    
    index = endpos
    while buffer[index] == 0x20: index += 1
    return index, fsv_name
  
  def get_fs_tree(self, buffer: ISUFile, offset: int = 0, **kwgs) -> FSFSTree:
    verbose = 'verbose' in kwgs and kwgs['verbose']
    root = kwgs['root'] if 'root' in kwgs else None

    for match in re.finditer(b'FSH1', buffer._file):
      index = match.end()

    if not index:
      if verbose: print("[-] Directory archive not found")
      return None

    size = to_ui32(buffer, index)
    if verbose: 
      print("[+] Found a directory archive(size=%d bytes, name='FSH1')" % size)

    index += 4
    to_ui16(buffer, index)
    
    index += 2
    index_len = to_ui32(buffer, index)
    if verbose: print("[+] Reading Index(size=%d bytes, offset=%d)...\n" % (index_len, index))
    
    index += 4
    tree = FSFSTree(root, attributes={
      'name': 'FSH1 Frontier Silicon Filesystem v1',
      'index_size': index_len,
      'archive_size': size,
      'offset': index -10
    })
    index = self._parse_entry(tree, index, index-10, buffer, 0, verbose)
    if verbose: print("\n[+] Successfully parsed the Index-Header\n")
    if root: root.append(tree)

    return tree

  def _parse_entry(self, tree, index, start, buffer, level, verbose: bool = False):
    entry_type = buffer[index]
    index += 1
    if entry_type == 0x00:
      return self._parse_file(tree, index, start, buffer, level, verbose)
    elif entry_type == 0x01:
      return self._parse_dir(tree, index, start, buffer, level, verbose)
    else:
      if verbose: print("[-] Invalid entry type: %#x" % entry_type)

  def _parse_file(self, tree, index, start, buffer, level, verbose: bool = False):
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
    
    entry = FSFSFile(tree, 'file', {
      'type': 0x00,
      'name': name,
      'size': file_size,
      'offset': file_offset,
      'compressed': 'True' if file_compression != file_size else "False",
      'compression_size': file_compression,
      'real_offset': start + file_offset
    })
    tree.append(entry)
    if verbose: 
      print("%s- %s type=0x00(file), offset=%d, compressed=%s, comp_size=%d" % (
        '|  '*level, name, file_offset, 
        "False" if file_compression == file_size else "True",
        file_compression
      ))
    return index

  def _parse_dir(self, tree, index, start, buffer, level=0, verbose=False) -> tuple:
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
    directory = FSFSFile(tree, 'dir', {
      'name': name,
      'type': 0x01,
      'entries': entries,
    })
    if verbose: print('%s| %s/ (entries=%d)' % ('|  '*level, name, entries))
    for _ in range(entries):
      index, offset_index = self._parse_entry(directory, index, start, buffer, level + 1, verbose)
    tree.append(directory)
    return index
  
  def get_compression_fields(self, buffer: ISUFile, offset: int = 0, **kwgs) -> list:
    verbose = 'verbose' in kwgs and kwgs['verbose']
    fields = []

    index = 2768
    while True:
      index, success = verify_skip(
        skip(buffer, index, MMI_BUF_SIZE_INDICATOR),
        "[-] Malformed indicator for buffer or size",
        verbose
      )
      if not success: return fields

      name_len = buffer[index]
      index += 1
      index, success = verify_skip(
        skip(buffer, index, [0x00, 0x04, 0x00]),
        "[-] Malformed byte code: expected 00 04 00",
        verbose
      )
      if not success: return fields

      try:
        # NOTE: name_len - 1 because name string is \0 terminated
        name = str(buffer[index:index+name_len - 1], 'utf-8')
        index += name_len
      except Exception as e:
        if verbose: print("[!] Exception: %s" % e)
        return fields

      data_size = 24 - name_len
      if data_size - 8 < 0:
        if verbose: print("[-] Malformed byte code: data size has to be > 8bytes")
        return fields
      
      index += data_size - 8
      size = to_ui32(buffer, index) # maybe to_ui24()
      index += 8

      if verbose: print("  - %s: %s=%d" % (name, 'Size' if 'Size' in name else 'Buffer', size))
      f0 = ISUCompressionField()
      f0._name = name
      f0._size = size
      fields.append(f0)

      if buffer[index] != 0x20:
        break
    
    return fields
    