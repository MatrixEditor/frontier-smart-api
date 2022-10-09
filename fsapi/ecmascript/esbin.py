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
__doc__ = '''
Frontier Smart products with the `Venice 8` module store a different directory
archive. Most of the files stored there are written in the ECMAScript language
and converted to binary files. They are most likely used to create the web
interface for the devices.

'''

__all__ = [
  'is_valid_ext', 'read_rstring', 'ECMAScriptHeader',
  'ECMAScript', 'ES_BIN_SUFFIX', 'ES_BIN_MAGIC', 'load_rstrings'
]

################################################################################
# esbin::imports
################################################################################
import re

from typing import Iterator
from ..isu import ioutils

################################################################################
# esbin::globals
################################################################################
ES_BIN_SUFFIX = r'\.es\d?\.bin'
'''
This module will accept files with an extension that matches this defined
regular expression. The following examples should show which file names 
are included:

>>> esbin.is_valid_ext('foobar.es.bin')
True
>>> esbin.is_valid_ext('foobar.es')
False
>>> esbin.is_valid_ext('foobar.es6.bin')
True
'''

ES_BIN_MAGIC = b'\x07\x00\xAD\xDE'
'''
ECMAScript binary files always start with header information and a file 
signature, which is ``07 00 AD DE``.
'''

ES_BIN_HEADER_LEN = 0x24

################################################################################
# esbin::functions
################################################################################
def is_valid_ext(name: str) -> bool:
  '''Applies the ES_BIN_SUFFIX pattern on the given string.
  
  :param name: usually the file name to test/ validate
  
  :rtype: bool:
  :returns: ``True`` if "``.es[:number:]?.bin``" was found in the given string;
            ``False`` otherwise.
  '''
  if not name or len(name) == 0:
    return False
  else:
    return re.search(ES_BIN_MAGIC, name) is not None

def read_rstring(buffer: bytes, offset: int) -> str:
  '''Reads a resource string.

  Warning, this method is context-sensitive, so a call should be done when
  the offset position points to the indicator before the size definition of 
  a resource string. The next index position would be calculated as follows:

  >>> val = read_rstring(buffer, offset)
  'fsapi'
  >>> next_pos += 8 + (len(val) * 2)
  14

  For information about how the resource strings are sturctured, please 
  refer to the fsapi-documentation.

  :param buffer: a byte buffer storing the raw bytes of the script file.
  :param offset: the offset position

  :rtype: str
  :returns: the resource string which was loaded
  '''
  offset, success = ioutils.skip(buffer, offset, (0x04, 0x00, 0x00, 0x00))
  if not success:
    raise SyntaxError('Invalid bytes at position %d: (04 00 00 00) expected' % offset)

  length = ioutils.to_ui32(buffer, offset)
  offset += 4
  idx = 0
  result = []

  while idx < length:
    chari = chr(buffer[offset])
    offset += 1
    if buffer[offset] >> 4 != 0x00:
      raise SyntaxError('Expected 0x00 at position %d' % offset)
    
    result.append(chari)
    offset += 1
    idx += 1
  
  # create the rstring by joining the loaded characters
  return ''.join(result)

def load_rstrings(buffer: bytes) -> 'ECMAScript':
  '''Attempts to read all resource strings from the given script buffer.

  This method will result in a packed ``ECMAScript`` object, which does not 
  contain any header information as well as resource flags that were set 
  before the resource section starts.
  
  :returns: A list of resource strings packed into an ECMAScript object.
  '''
  global_script = None

  for script_buf in buffer.split(ES_BIN_MAGIC):
    if len(script_buf) == 0: continue

    idx = script_buf.find(b'build') - 4
    if idx < 0:
      return []
    
    length = ioutils.to_ui32(script_buf, idx)

    idx += 4
    script = None
    if global_script is None:
      global_script = ECMAScript(str(script_buf[idx:idx+length], 'utf-8'))
      script = global_script
    else:
      script = ECMAScript(str(script_buf[idx:idx+length], 'utf-8'))
      global_script.subscripts.append(script)
    
    idx += len(script.name)
    flags1 = ioutils.to_ui32(script_buf, idx)
    flags2 = ioutils.to_ui32(script_buf, idx + 4)
    flags3 = ioutils.to_ui32(script_buf, idx + 8)

    idx += 12
    while idx < len(script_buf):
      if script_buf[idx] == 0x00:
        idx += 1
        continue

      rsc = read_rstring(script_buf, idx)
      idx += 8 + (len(rsc) * 2)
      script.components.append(rsc)

  return global_script

def load(buffer: bytes) -> 'ECMAScript':
  parser = ECMAScriptParser(next={ES_BIN_MAGIC: parse_header})
  if not parser.do_parse(buffer):
    raise SyntaxError('Could not parse ECMAScript')
  
  return parser.get_script()
    
def parse_header(parser: 'ECMAScriptParser', buffer: bytes, offset: int) -> int:
  # The offset does not has to be 4 (absolute position), because sub-scripts
  # may be placed after the main script. 
  header = parser.get_header()
  if not header.load(buffer, offset):
    raise SyntaxError('Could not load ECMAScript-Header')
  
  parser.set_next({b'\x7F\x00': parse_count})
  return offset + ES_BIN_HEADER_LEN

def parse_count(parser: 'ECMAScriptParser', buffer: bytes, offset: int) -> int:
  while True:
    offset, success = ioutils.skip(buffer, offset, (0x7F))
    if not success or buffer[offset + 2] != 0x7F: 
      break
    buffer += 2
  
  parser.set_next({b'\x6C', parse_lvar})
  return offset

def parse_lvar(parser: 'ECMAScriptParser', buffer: bytes, offset: int) -> int:
  '''Tries to parse a local variable definition.
  
  Usually, this statement constists of two indicator octets starting with ``6C``.
  Next, there is the resource string identifier (running number). 

  :returns: the provided offset + 2 if the running number is valid. 
  '''
  flags = buffer[offset]
  num = buffer[offset + 1]

  parser.get_script().repr += 'var {%d}' % num
  parser.set_next({b'\x3D'}) 
  return offset + 2

def parse_rscs(parser: 'ECMAScriptParser', buffer: bytes, offset: int) -> int:
  script = parser.get_script()
  script.name = read_rstring(buffer, offset)

  offset += 4 + (len(script.name) * 2)
  flags1 = ioutils.to_ui32(buffer, offset)
  flags2 = ioutils.to_ui32(buffer, offset + 4)
  flags3 = ioutils.to_ui32(buffer, offset + 8)

  offset += 12
  while offset < len(buffer):
    # NOTE: Sometimes it appers to be that there are filler bytes
    # of \x00. Therefore, this small statement wraps issues up
    if buffer[idx] == 0x00:
      idx += 1
      continue
    
    # WARNING: this loop is insecure for now, because it reads until
    # the end of a file is reached. Because it is possible to pack
    # multiple ECMAScript binaries into one large file, this method
    # most likely will fail on reading a resource string.
    rsc = read_rstring(buffer, offset)
    script.components.append(rsc)
    offset += 8 + (len(rsc) * 2)

  parser.set_next({b'\x07\x00\xAD\xDE', parse_header})
  return offset

################################################################################
# esbin::classes
################################################################################
class ECMAScriptHeader:
  '''A class representing the header section of a ECMAScript binary file.
  
  All inspected ECMAScript binary files contain a header definition, even if it
  is a sub-script definition. The length of this header is fixed to an amount
  of ``0x24`` bytes.

  This class contains a sequence-like implementation by providing the 
  ``__getitem__`` and ``__len__`` function (length is fixed to 8).
  '''
  def __init__(self) -> None:
    self.values = [0x00 for i in range(8)]

  def __getitem__(self, idx: int) -> int:
    if type(idx) != int:
      raise TypeError('Invalid index type')
    return self.values[idx]
  
  def __setitem__(self, idx: int, value: int):
    if 0 <= idx < len(self):
      self.values[idx] = value
  
  def __len__(self) -> int:
    return (ES_BIN_HEADER_LEN - 4) // 4
  
  def load(self, buffer: bytes, offset: int) -> bool:
    '''Tries to load the header values from the given buffer.

    :param buffer: the bytes to read

    :rtype: bool
    :returns: ``False`` if the header is malformed
    '''
    if len(buffer) < ES_BIN_HEADER_LEN:
      return False
    
    # REVISIT: After the ECMAScriptParser was implemented, the magic
    # bytes check is done one layer over this method.
    #
    # index, success = ioutils.skip(buffer, offset, ES_BIN_MAGIC)
    # if not success: return False
    for i in range(len(self)):
      self[i] = ioutils.to_ui32(buffer, offset)
      offset += 4
    return True

class ECMAScript:
  '''A class representing ECMAScript files in binary format.

  Files can contain different sub-scripts that are appended with the default
  ``ES_BIN_SUFFIX``.

  :param name: the file name for this script file
  :type name: str
  '''
  def __init__(self, name: str = None) -> None:
    self.subscripts = []
    self.components = []
    self.name = name
    self.header = ECMAScriptHeader()
    self.repr = ''
  
  def __iter__(self) -> Iterator['ECMAScript']:
    return iter(self.subscripts)
  
  def __getitem__(self, key) -> 'ECMAScript':
    return self.subscripts[key]
  
  def __str__(self) -> str:
    return '<ECMAScript %s>' % self.name

  def format(self) -> str:
    return self.repr.format(self.components)
  
class ECMAScriptParser:
  def __init__(self, next: dict = None) -> None:
    self.next = {} if not next else next
    self.script = ECMAScript()

  def do_parse(self, buffer: bytes) -> bool:
    if not buffer or len(buffer) == 0:
      return False
    
    index = 0
    stop = True
    while len(self.next) != 0 and index < len(buffer):
      # Iterate over all possible definitions:
      for pos in self.next:
        index, success = ioutils.skip(buffer, index, pos)
        # the mapped value is a function that takes exactly
        # three arguments (verbose is optional)
        if success:
          index = self.next[pos](self, buffer, index)
          stop = False
          break
      
      # the called function should return -1 on failure or 
      # raise an exception
      if stop: break
      if not stop: stop = True

    return index != -1

  def get_script(self) -> ECMAScript:
    return self.script
  
  def get_header(self) -> ECMAScriptHeader:
    return self.script.header
  
  def set_next(self, values: dict) -> None:
    if values is not None:
      self.next = values
  
  def __setitem__(self, key, value):
    if key not in self.next:
      self.next[key] = value

class ECMADefinition:
  def __init__(self) -> None:
    self.obj_idx: int = 0
    self.value: str = ''
