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

from .. import (
  ISUFile, 
  ISUHeader,
  FSFSTree,
  set_inspector
)

from .fs2026 import MMIInspector
from io import UnsupportedOperation
from ..ioutils import *

__all__ = [
  'OtaIspector', 'UBootConfig'
]

class UBootConfig(dict):
  pass

@set_inspector("ns/mmi/fs5332")
class OtaIspector(MMIInspector):
  def get_header(self, buffer: ISUFile, offset: int = 0, **kwgs) -> ISUHeader:
    header = super().get_header(buffer, offset, **kwgs)
    fsc = header.customisation

    if fsc.interface == 'mmi' and fsc.device_type == 'ns':
      return header

    raise ValueError("The given file is not of type 'ns'.")
    
  def get_fs_tree(self, buffer: ISUFile, offset: int = 0, **kwgs) -> FSFSTree:
    raise UnsupportedOperation()
  
  def get_partitions(self, buffer: ISUFile, **kwgs) -> list:
    raise UnsupportedOperation()

  def get_compression_fields(self, buffer: ISUFile, offset: int = 0, **kwgs):
    raise UnsupportedOperation()

  def get_uboot_config(self, buffer: ISUFile, **kwgs) -> UBootConfig:
    result = re.search(b'\x40\x00\x00\x80', buffer._file)
    if not result:
      raise ValueError("Could not find u-boot configuration")
    
    index = result.span()[1]
    manifest_size = to_ui16(buffer, index)
    index += 10

    config = buffer._file[index:index+manifest_size-1]
    rep_config = str(config, 'utf-8').split(' ')
    uboot = UBootConfig()

    last = None
    for i in range(len(rep_config)):
      e = rep_config[i]
      if not e: continue
      if '=' in e:
        values = e.split('=')
        uboot[values[0]] = values[1]
        last = values[0]
      elif last is not None:
        uboot[last] = uboot[last] + ' ' + e
      
    if 'verbose' in kwgs and kwgs['verbose']:
      print('[+] Found U-Boot configuration file:')
      for name in uboot:
        if name != 'mtdparts':
          print("  - %s: %s" % (name, uboot[name]))
        else:
          parts = uboot[name].split(':')
          print("  - %s: <mtd-id '%s'>" % (name, parts[0]))
          for partdef in parts[1].split(','):
            print("     | <part-def> %s" % partdef)

    return uboot
    
