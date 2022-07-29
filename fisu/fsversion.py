from re import match

RE_CUSTOM_BUFFER = r"^\w*-\w*-(FS\d{4})-\d{4}-\d{4}"
RE_VERSION_BUFFER = r"^\d*([.][\d]*\w*\d*){2}[.].*-.*"

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

class FSCutomization:
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
    
    if not match(RE_CUSTOM_BUFFER, buffer):
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
    # if not buffer or not match(RE_CUSTOM_BUFFER, buffer):
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