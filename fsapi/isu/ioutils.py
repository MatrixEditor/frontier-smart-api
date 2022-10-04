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
This small modules covers the little endian number creation. In future releases
there may be a reference to the ``python.struct`` library to delegate the creation.
'''

__all__ = [
  'to_ui32', 'to_ui24', 'to_ui16', 'skip', 'verify_skip'   
]

def to_ui32(buffer: bytes, index: int = 0) -> int:
  '''Utility function to create an unsigned 32 bit integer (little endian).

  >>> ioutils.to_ui32([1, 2, 3, 4])
  0x4321

  :param buffer: a byte-buffer object implementing the ``__get_item__`` function
  :param index: the offset index where to start 
  
  :returns: an unsigned 32 bit integer (4 bytes)
  '''
  return (
    buffer[index] | buffer[index + 1] << 8 | buffer[index + 2] << 16 | buffer[index + 3] << 24
  )

def to_ui24(buffer: bytes, index: int = 0) -> int:
  '''Utility function to create an unsigned 24 bit integer (little endian).

  :param buffer: a byte-buffer object implementing the ``__get_item__`` function
  :param index: the offset index where to start 
  
  :returns: an unsigned 24 bit integer (3 bytes)
  '''
  return (
    buffer[index] | buffer[index + 1] << 8 | buffer[index + 2] << 16
  )

def to_ui16(buffer: bytes, index: int = 0) -> int:
  '''Utility function to create an unsigned 16 bit integer (little endian).

  :param buffer: a byte-buffer object implementing the ``__get_item__`` function
  :param index: the offset index where to start 
  
  :returns: an unsigned 16 bit integer (2 bytes)
  '''
  return buffer[index] | buffer[index + 1] << 8

def skip(buffer: bytes, start: int, pattern: list) -> tuple:
  '''Utility function to skip the given pattern in the provided buffer.
  
  This method returns a ``tuple`` with the next index and ``bool`` value indicating
  whether the performed skip was successfull.

  >>> ioutils.skip([0, 1, 2, 3, 4], 0, [0, 1, 2])
  (3, True)
  >>> ioutils.skip([0, 1, 2], 0, [5, 6, 7])
  (0, False)

  :param buffer: a byte-buffer object implementing the ``__get_item__`` function
  :param index: the offset index where to start 
  :param pattern: an object implementing the ``__get_item__`` function storing
                  the bytes to skip
  
  :returns: a tuple containing the next index and a flag that indeicates whether
            this method has failed.
  '''
  if not buffer or not pattern:
    return start, False
  
  pos = 0
  while True:
    if pos >= len(pattern):
      break
    
    if buffer[pos+start] != pattern[pos]:
      return start, False
    pos += 1
  
  return pos+start, True

def verify_skip(values: tuple, message: str = None, verbose: bool = False) -> bool:
  '''Utility wrapper for printing a message if the ``skip()`` method fails.

  A sample usage of this method could be the following:

  >>> ioutils.verify_skip(skip([1, 2], 0, [3, 4]), "Skip failed!", verbose=True)
  Skip failed!

  :param values: the result returned by the skip-method
  :param message: the message to print if the ``values`` contain a false-flag
  :param verbose: specifies whether the ``message`` should be printed

  :returns: the provided `values` 
  '''
  index, success = values
  if not success:
    if verbose: print(message)
    return index, False
  return index, True 