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

from typing import overload
from .fsfs import FSFSTree, FSFSFile

__all__ = [
  "ISUFile", "ISUInspector", "ISUCompressionField", "ISUHeader",
  "ISU_MAGIC_BYTES", "SetInspector"
]

ISU_MAGIC_BYTES = [0x76, 0x11, 0x00, 0x00]

class ISUFile:
  @overload
  def __init__(self, res: str) -> None: ...
  @overload
  def __init__(self, res: bytes) -> None: ...

  def __init__(self, res) -> None:
    self._file = None
    self.v = 0
    if type(res) == str:
      self._file = open(res, 'rb').read()
    elif type(res) == bytes:
      self._file = res
    else:
      self._file = res.read()

    # accessable attributes
    self.version = None
    self.customisation = None
  
  def __getitem__(self, key):
    return self._file[key]
  
  def pull(self) -> int:
    pos = self.v
    self.v += 1
    return self[pos]
  
  @property
  def position(self) -> int:
    return self.v

class ISUCompressionField:
  def __init__(self) -> None:
    self._name = None
    self._size = -1

  @property
  def name(self) -> str:
    return self._name
  
  @property
  def size(self) -> int:
    return self._size
  
  def __bytes__(self) -> bytes:
    raise NotImplementedError()

  def __str__(self) -> str:
    raise NotImplementedError()

class ISUHeader:
  def __init__(self) -> None:
    self._meos_version = 0
    self._version = None
    self._customisation = None
    self._size = -1
  
  @property
  def meos_version(self) -> int:
    return self._meos_version

  @property
  def version(self):
    return self._version

  @property
  def customisation(self):
    return self._customisation

  @property
  def size(self) -> int:
    return self._size

  def __repr__(self) -> str:
    return '<ISUHeader size=%d>' % self.size

INSPECTOR_TABLE = {}

class ISUInspector:

  @staticmethod
  def getInstance(name: str) -> 'ISUInspector':
    return INSPECTOR_TABLE[name]()

  def get_fs_tree(self, buffer: ISUFile, offset: int = 0, **kwgs) -> FSFSTree:
    pass

  def get_header(self, buffer: ISUFile, offset: int = 0, **kwgs) -> ISUHeader:
    pass

  def get_compression_fields(self, buffer: ISUFile, offset: int = 0, **kwgs) -> list:
    pass

def SetInspector(name: str):
  def add_inspector(insp):
    if name not in INSPECTOR_TABLE:
      INSPECTOR_TABLE[name] = insp
    return insp
  return add_inspector