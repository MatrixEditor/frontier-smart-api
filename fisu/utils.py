
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
