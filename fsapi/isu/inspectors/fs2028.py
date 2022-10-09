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
  ISUCompressionField,
  set_inspector
)

from ..ioutils import *

from .fs2026 import MMIInspector, MMI_BUF_SIZE_INDICATOR

__all__ = [
  'FS2028MMIInspector'
]

@set_inspector('ir/mmi/fs2028')
class FS2028MMIInspector(MMIInspector):

  def get_compression_fields(self, buffer: ISUFile, offset: int = 0, **kwgs) -> list:
    verbose = 'verbose' in kwgs and kwgs['verbose']
    fields = []

    if verbose: print("[+] Declared Fields:")
    # NOTE: The index can not be static due to the fact that the declared 
    # fields' position is changing dynamically in the 0200 firmware files.
    index = 2768
    pos = re.search(b'DecompBuffer', buffer._file)
    if not pos:
      return fields

    index = pos.span()[0] - 8
    while True:
      # Additional field CompSSSize in FS2028 starts with 
      # a different indicator [0x18, 0x00, 0x00, 0x53]
      iszcompss = buffer[index] == 0x18
      index, success = verify_skip(
        skip(buffer, index, MMI_BUF_SIZE_INDICATOR if not iszcompss else [0x18, 0x00, 0x00, 0x53]),
        "[-] Malformed indicator for buffer or size\n",
        verbose
      )
      if not success: return fields

      name_len = buffer[index]
      index += 1
      index, success = verify_skip(
        skip(buffer, index, [0x00, 0x04, 0x00] if not iszcompss else [0x00, 0x00, 0x5A]),
        "[-] Malformed byte code: expected 00 04 00 or 00 00 5A\n",
        verbose
      )
      if not success: return fields

      try:
        # NOTE: name_len - 1 because name string is \0 terminated
        name = str(buffer[index:index+name_len - 1], 'utf-8')
        index += name_len
      except Exception as e:
        if verbose: print("[!] Exception: %s\n" % e)
        return fields

      data_size = 24 - name_len
      if data_size - 8 < 0:
        if verbose: print("[-] Malformed byte code: data size has to be > 8bytes\n")
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
        if buffer[index] == 0x18: continue
        break
    
    print()
    return fields