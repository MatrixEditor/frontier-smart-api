import urllib3
import re
import xml.etree.ElementTree as xmltree
import fsapi

###############################################################################
# Constants
###############################################################################

ISU_FILE_PROVIDER_HOST = 'update.wifiradiofrontier.com'

ISU_REQUEST_HEADERS = {
  'User-Agent': "FSL IR/0.1",
  'Connection': "Close"
}

# MAC-Address structure for internet radios:
# '002261' + 6 characters from hex-alphabet
RE_FSIR_MAC_ADDR = r"^(002261)[\d\w]{6}$"

# Example: 2.10.13.EX65638-1A11
RE_FS_VERSION = r"\d*[.]\d*[.]\d*\w*\d?[.]EX\d{5}-\d*\w*\d*"

# Example: ir-mmi-FS2026-0500-0037
RE_FS_CUSTOMISATION = r"\w*-\w*-FS\d{4}(-\d{4}){2}"

###############################################################################
# Classes
###############################################################################

class ISUSoftwareElement:
  def __init__(self, customisation: str = None, version: str = None,
               download_url: str = None, mandatory: bool = False,
               md5hash: str = None, product: str = None, size: int = 0,
               vendor: str = 'Frontier Silicon', summary: str = None) -> None:
    self.customisation = customisation
    self.version = version
    self.download_url = download_url
    self.mandatory = mandatory
    self.md5hash = md5hash
    self.product = product
    self.vendor = vendor
    self.summary = summary
    self.size = size
  
  def __str__(self) -> str:
    return "Software(c='%s', v='%s', mandatory=%s, size=%d, path='%s')" % (
      self.customisation, self.version, self.mandatory, self.size, self.download_url
    )

  def loadxml(self, element: xmltree.Element):
    if not element: return
    self.customisation = element.get('customisation')
    self.version = element.get('version')
    self.download_url = element.find('download').text
    self.mandatory = element.find('mandatory').text == 'True'
    self.product = element.find('product').text
    self.size = int(element.find('size').text)
    self.md5hash = element.find('md5').text
    self.summary = element.find('summary').text
    self.vendor = element.find('vendor').text

###############################################################################
# Functions
###############################################################################

def _url_find_update_add_parameters(url: str, parameters: dict) -> str:
  uri = '/FindUpdate.aspx?'
  return url + uri + '&'.join(['%s=%s' % (key, parameters[key]) for key in parameters])

def isu_find_update(mac: str, customisation: str, version: str, 
                    verbose: bool = False, 
                    netconfig: fsapi.FSNetConfiguration = None) -> dict:
  if not re.match(RE_FSIR_MAC_ADDR, mac):
    if verbose: print("[-] Failed to find an update: malformed MAC-Address")
    return None
  
  if not re.match(RE_FS_CUSTOMISATION, customisation):
    if verbose: print("[-] Failed to find an update: malformed customisation string")
    return None

  if not re.match(RE_FS_VERSION, version):
    if verbose: print("[-] Failed to find an update: malformed version string")
    return None

  url = _url_find_update_add_parameters('https://' + ISU_FILE_PROVIDER_HOST, {
    'mac': mac,
    'customisation': customisation,
    'version': version
  })

  if netconfig:
    response = netconfig.delegate_request('GET', url, ISU_REQUEST_HEADERS)
    response.chunked
  else:
    pool = urllib3.HTTPSConnectionPool(host=ISU_FILE_PROVIDER_HOST, headers=ISU_REQUEST_HEADERS)
    response = pool.request('GET', url)
    pool.close()

  values = {'update_present': False}
  if response.status == 404:
    if verbose: print("[-] Update not found: invalid version or customisation")
    return None
  elif response.status == 304:
    if verbose: print("[-] No Update available for: ", customisation)
    return values
  
  if response.status != 200:
    if verbose: print("[-] Unexpected result code:", response.status)
    return values
  else:
    try:
      values['headers'] = response.headers
      content = str(response.data, 'utf-8')

      pos = content.find('<?xml')
      if pos == -1:
        if verbose: print("[-] Unexpected result: XML-Content missing")
        return values
      else:
        content = content[pos:pos+content.find('</updates>', pos)+9]
        root = xmltree.fromstring(content)
        updates = []
        for software in root:
          s = ISUSoftwareElement()
          s.loadxml(software)
          updates.append(s)

        values['updates'] = updates
        values['update_present'] = True
        return values
    except Exception as e:
      if verbose: print("[-] Error while parsing response: %s" % e)
      return values

def isu_get_update(path: str, url: str = None, software: ISUSoftwareElement = None,
                   verbose: bool = False,
                   netconfig: fsapi.FSNetConfiguration = None):
  if not url and (not software or not software.download_url):
    if verbose: print("[-] Invalid choice of parameters: either url or software has to be nonnull")
    return
  
  url = url if url else software.download_url
  if netconfig:
    response = netconfig.delegate_request('GET', url, ISU_REQUEST_HEADERS, preload_content=False)
    response.chunked
  else:
    if 'https' not in url: url = url.replace('http', 'https')
    pool = urllib3.HTTPSConnectionPool(host=ISU_FILE_PROVIDER_HOST, headers=ISU_REQUEST_HEADERS, timeout=5)
    response = pool.request('GET', url, preload_content=False)
    
  if response.status != 200:
    if verbose: print("[-] Unexpected result code:", response.status)
    response.release_conn()
    return
  
  with open(path, 'wb') as _res:
    for chunk in response.stream(4096*16):
      if chunk: _res.write(chunk)
  response.release_conn()


  
  
  
  
  