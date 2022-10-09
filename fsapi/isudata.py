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
The backend used to find and download updates is located at ``update.wifiradiofrontier.com.``
To interact with the underlaying API, the isudata-module comes with two main-methods:

* ``isu_new_url``, 
* ``isu_find_update`` and
* ``isu_get_update``.

'''

import urllib3
import re
import xml.etree.ElementTree as xmltree

from .netconfig import FSNetConfiguration

__all__ = [
  "ISU_FILE_PROVIDER_HOST", "ISUSoftwareElement", "isu_find_update",
  "isu_get_update", "isu_new_url"
]

###############################################################################
# Constants
###############################################################################

ISU_FILE_PROVIDER_HOST = 'update.wifiradiofrontier.com'
ISU_EDGE_PROVIDER_HOST = 'nuv-isu-cdn.azureedge.net'
# https://nuv-isu-cdn.azureedge.net/srupdates/srupdates/ir-cui-FS2340-0000-0146/ir-cui-FS2340-0000-0146_V4.5.13.707296-1A20.isu.bin
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
  '''This class contains all information needed to distinguish an update entry. 
  
  Use the ``loadxml`` function to import data from an XML-Element.

  :param customisaton: The customisation string for this element.
  :param version: The version string for this element.
  :param download_url: The URL where the firmware binary is located
  :param mandatory: Indicates whether this update is mandatory
  :param md5hash: The calculated md5Hash for the firmware binary
  :param product: The product's name
  :param vendor: usually Frontier Smart
  :param size: the file's size
  '''
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
    '''Imports data from the given XML-Element.'''
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
                    netconfig: FSNetConfiguration = None) -> dict:
  '''Tries to find updates for the given version and customisation.
  
  :param mac: The MAC-Address string of a frontier silicon device in the following 
              format: ``002261xxxxxx``. This string must start with ``002261``.
  :param customisation: Information about the used interface, module and version 
                        number.
  :param version: As the name already states, the full version string.
  :param verbose: if enabled/True, error messages will be printed to stdout
  :param netconfig: if a custom configuration like a proxy should be used, this 
                    object can be passed as a parameter

  :returns: ``None`` if an error occurred or a dictionary with the following structure 
            if one ore more updates are present::

              return {
                'update_present': bool,
                'headers': dict,
                'updates': list[ISUSoftwareElement]
              }
  '''
  
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
                   netconfig: FSNetConfiguration = None):
  '''Tries to download and save the firmware binary located at the given URL.

  :param path: an absolute or relative path to the output file
  :param url: optional the direct download link - if not set, the software parameter 
              must be defined
  :param software: the software object containing the relevant data for downloading
                   the update file
  :param verbose: if enabled/True, error messages will be printed to stdout
  :param netconfig: if a custom configuration like a proxy should be used, this object
                    can be passed as a parameter
  '''

  if not url and (not software or not software.download_url):
    if verbose: print("[-] Invalid choice of parameters: either url or software has to be nonnull")
    return
  
  url = url if url else software.download_url
  if netconfig:
    response = netconfig.delegate_request('GET', url, ISU_REQUEST_HEADERS, preload_content=False)
    response.chunked
  else:
    # manager = urllib3.PoolManager(headers=ISU_REQUEST_HEADERS, timeout=5)
    if 'https' not in url: url = url.replace('http', 'https')
    pool = urllib3.HTTPSConnectionPool(host=url.split("/")[2], headers=ISU_REQUEST_HEADERS, timeout=5)
    response = pool.request('GET', url, preload_content=False)
    
  if response.status != 200:
    if verbose: print("[-] Unexpected result code:", response.status)
    response.release_conn()
    return
  try:
    with open(path, 'wb') as _res:
      for chunk in response.stream(4096*16):
        if chunk: _res.write(chunk)
  except:
    print('[-] TImeout Error...')
  response.release_conn()

def isu_new_url(name: str) -> str:
  '''An URL generator for the given product descriptor.

  :param name: the customisation and version put toghether wither with 
               a '`_V`'.
  :returns: the newly generated url where the firmware can be downloaded
  '''
  parts = name.split('-')
  fs_part = None
  url = None

  # NOTE: Some firmware binaries contain different sub-interfaces, so
  # the FSXXXX module definition will be shift to the right.
  for f in filter(lambda x: 'FS' in x, parts):
    fs_part = f
    break

  if fs_part is not None:
    if fs_part == 'FS2340':
      customisation = name.split('_V')[0]
      url = 'https://%s/srupdates/srupdates/%s/%s.isu.bin' % (
        ISU_EDGE_PROVIDER_HOST, customisation, name
      )
    elif fs_part == 'FS5332':
      customisation = name.split('_V')[0]
      url = 'https://%s/nsupdates/nsupdates/%s/%s.ota.bin' % (
        ISU_EDGE_PROVIDER_HOST, customisation, name
      )
    else:
      url = 'https://%s/Update.aspx?f=/updates/%s.isu.bin' % (
        ISU_FILE_PROVIDER_HOST, name.replace('_V', '.')
      )

  return url
  
