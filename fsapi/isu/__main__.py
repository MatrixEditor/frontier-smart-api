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

################################################################################
# ISU-Inspector::import
################################################################################
import re
import os
import argparse
import zlib

from time import sleep
from io import UnsupportedOperation
from . import *

################################################################################
# ISU-Inspector::globals
################################################################################
__BANNER__ = """\
    ╦╔═╗╦ ╦   ╦┌┐┌┌─┐┌─┐┌─┐┌─┐┌┬┐┌─┐┬─┐
    ║╚═╗║ ║───║│││└─┐├─┘├┤ │   │ │ │├┬┘
    ╩╚═╝╚═╝   ╩┘└┘└─┘┴  └─┘└─┘ ┴ └─┘┴└─
───────────────────────────────────────────
"""

ALLOWED_SUFFIXES = ('isu.bin', 'ota.bin')

################################################################################
# ISU-Inspector::functions
################################################################################
def parse_header(fp: ISUFile, inspector: ISUInspector, root: FSFSFile = None,
                 verbose: bool = False) -> None:
  try: # read and print header
    header = inspector.get_header(fp, verbose=verbose)
    if header is not None and root is not None:
      root.append(FSFSFile('header', attributes={
        'size': header.size,
        'version': str(header.version),
        'customisation': str(header.customisation)
      }))
    sleep(1)
  except UnsupportedOperation or NotImplementedError as e:
    print('ERROR - FATAL: ', str(e))

  try: # read and print partitions
    partitions = inspector.get_partitions(fp, verbose=verbose)
    if partitions is not None and root is not None:
      p_e = FSFSFile('partitions', {'amount': len(partitions)})
      for partition in partitions:
        p_e.append(FSFSFile('partition', attributes={
          'type': partition._type,
          'number': partition.partition,
          'is_web_partition': partition.is_web_partition()
        }))
      root.append(p_e)
    sleep(1)
  except UnsupportedOperation or NotImplementedError as e:
    print('ERROR - FATAL: ', str(e))

  try: # read and print uboot
    if type(inspector) == OtaIspector:
      config = inspector.get_uboot_config(fp, verbose=verbose)
      if config is not None and root is not None:
        # REVISIT: maybe iterate over mtdparts and add them
        # individually.
        p_e = FSFSFile('uboot', attributes=config)
        root.append(p_e)
      sleep(1)
  except UnsupportedOperation or NotImplementedError as e:
    print('ERROR - FATAL: ', str(e))

  try: # read and print compression/decompression fields
    fields = inspector.get_compression_fields(fp, verbose=verbose)
    if fields is not None and root is not None:
      p_e = FSFSFile('FieldList', {})
      for field in fields:
        p_e.append(FSFSFile(field.name, {'size': field.size}))
      root.append(p_e)
    sleep(1)
  except UnsupportedOperation or NotImplementedError as e:
    print('ERROR - FATAL: ', str(e))

def parse_directory_archive(fp: ISUFile, inspector: ISUInspector, 
                            root: FSFSFile = None, verbose: bool = False):
  try: # read and print header
    tree = inspector.get_fs_tree(fp, verbose=verbose)
    if tree is not None:
      root.append(tree)
  except UnsupportedOperation or NotImplementedError as e:
    print('ERROR - FATAL:', str(e))

def save_dir_entry(root: FSFSFile, buffer: bytes, path: str, start: int):
  name = root.get_attribute('name')
  if root.get_attribute('type') == 0x00: # file
    compressed = root.get_attribute('compressed') == 'True'
    #if compressed: name += '.zlib'
    with open(path + name, 'wb') as res:
      off = start + root.get_attribute('offset')
      if root.get_attribute('compressed') == 'True':
        dc_data = zlib.decompress(buffer[off:off+root.get_attribute('compression_size')])
        #res.write(buffer[off:off+root.get_attribute('compression_size')])
        res.write(dc_data)
      else:
        res.write(buffer[off:off+root.get_attribute('size')])
  else:
    if name == 'root': name = 'fsh1'
    try: os.mkdir(path + name)
    except: pass
    for element in root:
      save_dir_entry(element, buffer, path + name + '/', start)

def get_inspector_from_file(name: str) -> ISUInspector:
  name = name.split('/')[-1].split('-')
  # NOTE: The inspector can be retrieved by replacing the '-' with a '-'
  # for the first three elements (if 'FS' is present in the third one)
  if 'FS' in name[2]:
    res_path = '/'.join(name[:3])
  else:
    res_path = name[0]
    pos = 1
    next_path = []
    # NOTE: some inspectors contain sub-type definitions, which are added
    # with a '.' in the descriptor string: e.g. 'ir/mmi.16m/fs2026'
    while 'FS' not in name[pos]:
      next_path.append(name[pos])
      pos += 1
    res_path = '%s/%s/%s' % (res_path, '.'.join(next_path), name[pos])

  return ISUInspector.getInstance(res_path)

def extract_bytes(fp: ISUFile, root: FSFSFile, nspace: dict) -> None:
  name = root.get_attribute('path').split('/')[-1]
  if name.endswith(ALLOWED_SUFFIXES[0]) or name.endswith(ALLOWED_SUFFIXES[1]):
    name = name[:-8]

  path = root.get_attribute('path') + '/' + name
  if nspace['header']:
    try:
      with open('%s.header.bin' % path, 'wb') as ofp:
        ofp.write(fp._file[:MMI_HEADER_LENGTH])
    except OSError:
      print('[i] Could not save header file to "%s.header.bin"' % path)
  
  if nspace['archive']:
    try:
      fsh = root.get_element('fsh1')
      if fsh is not None:
        path = '_%s.extracted/' % path
        try: os.mkdir(path) 
        except: pass
      
        for element in fsh:
          save_dir_entry(element, fp._file, path, start=fsh.get_attribute('offset'))
    except OSError:
      print('[i] Could not save directory archive')
  
  if nspace['core']:
    size = -1
    for field in root.get_element('FieldList'):
      if field.tag == 'CompSize':
        size = field.get_attribute('size')
    
    index = fp._file.find(b'\x1B\x00\x55\xAA')
    if size != -1 and index != -1:
      try:
        with open('%s.core.bin' % path, 'wb') as ofp:
          ofp.write(fp._file[index:index+size])
      except OSError:
        print('[i] Could not save binary core to "%s.core.bin"' % path)

################################################################################
# ISU-Inspector::main
################################################################################
if __name__ == '__main__':
  # Parser-Args
  parser = argparse.ArgumentParser()
  parser.add_argument('-if', type=str, required=True, 
    help="The input file (optional *.isu.bin or *.ota.bin extension)"
  )
  parser.add_argument('-of', type=str, required=False,
    help="The output file (Format: XML)."
  )
  parser.add_argument('--verbose', action='store_true', default=False,
    help="Prints useful information during the specified process."  
  )
  parser.add_argument('-insp', type=str, required=False, default=None,
    help="Sets the ISUInspector descriptor, which will be used to retrieve\n\
      the inspector instance."
  )

  group_info = parser.add_argument_group("information gathering")
  group_info.add_argument('--header', action='store_true', default=False, 
    help="Parses the header of the given file and extracts information."
  )
  group_info.add_argument('--archive', action='store_true', default=False, 
    help="Parses the directory archive."
  )
  
  group_extract = parser.add_argument_group("extract data")
  group_extract.add_argument('-e', '--extract', action='store_true', default=False,
    help="Extract data (usually combined with other parameters)."
  )
  group_extract.add_argument('--core', action='store_true', default=False,
    help="Extract the compressed core partition source."
  )

  nspace = parser.parse_args().__dict__
  verbose = nspace['verbose']

  if verbose: print(__BANNER__)
  if 'if' not in nspace:
    print('[-] Input file not specified -> Quitting...')
    exit(1)
  
  ipath = nspace['if']
  opath = nspace['of'] if 'of' in nspace else None
  tree  = FSFSFile('isu', {'path': ipath})

  try:
    fp = ISUFile(ipath)
  except OSError:
    print('[i] Could not open input file (%s)' % ipath)

  if 'insp' in nspace and nspace['insp']:
    inspector = ISUInspector.getInstance(nspace['insp'])
  else:
    inspector = get_inspector_from_file(ipath)

  if nspace['header']:
    parse_header(fp, inspector, tree, verbose)
  
  if nspace['archive']:
    parse_directory_archive(fp, inspector, tree, verbose)
  
  if opath and tree is not None:
    try:
      with open(opath, 'w') as ofp:
        ofp.write('<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>\n')
        ofp.write(tree.toXml())
      
      if verbose: print('[i] Saved XML-output to', opath)
    except OSError:
      print('[i] Could not save output to file (%s)' % opath)

  if nspace['extract']:
    extract_bytes(fp, tree, nspace)

