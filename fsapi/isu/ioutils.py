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

__all__ = [
  'to_ui32', 'to_ui24', 'to_ui16', 'skip', 'verify_skip'   
]

def to_ui32(buffer: bytes, index: int = 0) -> int:
  return (
    buffer[index] | buffer[index + 1] << 8 | buffer[index + 2] << 16 | buffer[index + 3] << 24
  )

def to_ui24(buffer: bytes, index: int = 0) -> int:
  return (
    buffer[index] | buffer[index + 1] << 8 | buffer[index + 2] << 16
  )

def to_ui16(buffer: bytes, index: int = 0) -> int:
  return buffer[index] | buffer[index + 1] << 8

def skip(buffer: bytes, start: int, pattern: list) -> tuple:
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
  index, success = values
  if not success:
    if verbose: print(message)
    return index, False
  return index, True 