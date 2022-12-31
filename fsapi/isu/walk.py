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

from fsapi.isu.product import FSCustomisation, FSVersion
from .fsfs import FSFSTree, FSFSFile

__all__ = [
  "ISUFile", "ISUInspector", "ISUCompressionField", "ISUHeader",
  "ISU_MAGIC_BYTES", "set_inspector", "ISUPartition"
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
  
  def get_buffer(self) -> bytes:
    return self._file

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
  def __init__(self, meos_version: int = 0, version: FSVersion = None,
               customisation: FSCustomisation = None, size: int = -1) -> None:
    self._meos_version = meos_version
    self._version = version
    self._customisation = customisation
    self._size = size
  
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

class ISUPartition:
  ENTRY_END = 1
  ENTRY_PT = 0

  PT_10_CRC = (0x06, 0x02, 0x1F, 0x2B)
  PT_20_CRC = (0x0A, 0x02, 0x7E, 0xDB)

  def __init__(self, number: int = -1, entry_type: int = 0) -> None:
    self._number = number
    self._type = entry_type

  @property
  def partition(self) -> int:
    return self._number

  @partition.setter
  def partition(self, value: int):
    self._number = value

  def get_crc(self) -> frozenset:
    if self.partition == 1:
      return ISUPartition.PT_10_CRC
    elif self.partition == 2:
      return ISUPartition.PT_20_CRC
    else:
      return frozenset()
  
  def is_web_partition(self) -> bool:
    return self.partition == 2

  def __repr__(self) -> str:
    return '<Partition %d: web=%s>' % (self.partition, self.is_web_partition())

INSPECTOR_TABLE = {}

class ISUInspector:

  @staticmethod
  def getInstance(name: str) -> 'ISUInspector':
    return INSPECTOR_TABLE[name.lower()]()

  def get_fs_tree(self, buffer: ISUFile, offset: int = 0, **kwgs) -> FSFSTree:
    pass

  def get_header(self, buffer: ISUFile, offset: int = 0, **kwgs) -> ISUHeader:
    pass

  def get_compression_fields(self, buffer: ISUFile, offset: int = 0, **kwgs) -> list:
    pass

  def get_partitions(self, buffer: ISUFile, **kwgs) -> list:
    pass

def set_inspector(name: str):
  def add_inspector(insp):
    if name not in INSPECTOR_TABLE:
      INSPECTOR_TABLE[name] = insp
    return insp
  return add_inspector