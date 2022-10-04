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
In order to store and identify each part of the firmware-version and -customisation 
string, the classes ``FSCustomisation`` and ``FSVersion`` were created. Additionally,
there are two RegEx-strings that are used to verify the given verison or customisation
string::

  # e.g. ir-mmi-FS2026-0500-0015
  RE_CUSTOMISATION = r"^\w*-\w*-(FS\d{4})-\d{4}-\d{4}"
  
  # e.g. 2.6.17c4.EX53330-V1.08
  RE_VERSION = r"^\d*([.][\d]*\w*\d*){2}[.].*-.*"

Both classes mentioned above can be created with and without their attributes. To load
a verison or customisation string, you can use the ``loads()`` method in both classes.
'''


import re

__all__ = [
  "FSCustomisation", "FSVersion", "RE_CUSTOMISATION", "RE_VERSION",
  "FSVERSION_MODULE_TYPES"
]

RE_CUSTOMISATION = r"^\w*-\w*-(FS\d{4})-\d{4}-\d{4}"
RE_VERSION = r"^\d*([.][\d]*\w*\d*){2}[.].*-.*"

FSVERSION_MODULE_TYPES = {
  'FS2025': 'Venice 5',
  'FS2026': 'Venice 6',
  'FS2027': 'Venice 7',
  'FS2028': 'Venice 8',
  'FS2029': 'Venice 9',
  'FS2052': 'Verona',
  'FS2445': 'Verona 2',
  'FS2230': 'Tuscany'
}

class FSCustomisation:
  def __init__(
    self,
    device_type: str = None,
    interface: str = None,
    module_type: str = None,
    module_version: str = None
  ) -> None:
    self.device_type = device_type
    self.interface = interface
    self.module_type = module_type
    self.module_version = module_version
    self.module_name = None
    self.repr = None

  def loads(self, buffer: str, verbose: bool = False):
    if not buffer:
      return
    
    if not re.match(RE_CUSTOMISATION, buffer):
      if verbose: print("[-] Unable to load FSVersion: malformed input")
      return
    
    content = buffer.split('-')
    self.device_type = content[0]
    self.interface = content[1]
    self.module_type = content[2]
    self.module_version = content[3]
    self.repr = buffer

    if self.module_type in FSVERSION_MODULE_TYPES:
      self.module_name = FSVERSION_MODULE_TYPES[self.module_type]

  def get_module_name(self):
    return self.module_name

  def __str__(self) -> str:
    return self.repr

class FSVersion:
  def __init__(
    self,
    firmware_version: str = None,
    sdk_version: str = None,
    revision: str = None,
    branch: str = None
  ) -> None:
    self.firmware_version = firmware_version
    self.repr = None
    self.sdk_version = sdk_version
    self.revision = revision
    self.branch = branch

  def loads(self, buffer: str):
    # if not buffer or not match(RE_CUSTOMISATION, buffer):
      # return
    
    index = buffer.rindex('.')
    self.firmware_version = buffer[:index]
    self.sdk_version = 'IR' + self.firmware_version + ' SDK'
    temp = buffer[index+1:]
    self.revision = temp[2:7]
    self.branch = temp[temp.index('-')+1:]
    self.repr = buffer

  def __str__(self) -> str:
    return self.repr
