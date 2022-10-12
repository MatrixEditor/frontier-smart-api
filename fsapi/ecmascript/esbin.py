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
  'is_valid_ext', 'Decompiler', 'ES_BIN_SUFFIX', 'ES_BIN_MAGIC'
]

################################################################################
# esbin::imports
################################################################################
import re
import subprocess
import sys

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
    return re.search(ES_BIN_SUFFIX, name) is not None

class Decompiler:
  def __init__(self, decompiler_path: str, file_path: str) -> None:
    self.dpath = decompiler_path
    self.fpath = file_path
    self.done = False
    self.sourcecode = None

  def __enter__(self) -> 'Decompiler':
    if sys.platform == 'win32':
      raise SystemError('Unsupported OS')

    self.do_final()
    return self
  
  def __exit__(self, type, value, traceback) -> None:
    del self.sourcecode

  def do_final(self) -> str:
    if self.done:
      return self.sourcecode

    if not is_valid_ext(self.fpath):
      raise ValueError('Invalid script file')
  
    result = subprocess.run(args=[self.dpath, self.fpath], shell=True, capture_output=True)
    result.check_returncode()

    self.sourcecode = result.stdout.decode('utf-8')
    self.done = True
    return self.sourcecode
  
  def __str__(self) -> str:
    if not self.done:
      return self.do_final()
    return self.sourcecode

  @property
  def code(self) -> str:
    return self.sourcecode
