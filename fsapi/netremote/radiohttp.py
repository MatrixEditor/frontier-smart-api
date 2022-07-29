import urllib3
import xml.etree.ElementTree as xmltree

from ..netconfig import FSNetConfiguration

RADIO_HTTP_DEFAULT_PIN = '1234'

GET             = 'GET'
GET_MULTIPLE    = 'GET_MULTIPLE'
SET             = 'SET'
SET_MULTIPLE    = 'SET_MUTLIPLE'
LIST_GET        = 'LIST_GET'
LIST_GET_NEXT   = 'LIST_GET_NEXT'
CREATE_SESSION  = 'CREATE_SESSION'
DELETE_SESSION  = 'DELETE_SESSION'

class NodeError(Exception):
  pass

class ApiResponse:
  def __init__(self, node_class, xml_root: xmltree.Element = None) -> None:
    self.xml_root = xml_root
    self.node_class = node_class
    self.status = None
    self.content = None

  def parsexml(self, content: bytes, as_list: bool = False):
    self.xml_root = xmltree.fromstring(content)
    self.status = self.xml_root.find('status').text
    if self.status != 'FS_OK':
      return

    self.content = self.node_class()
    prototype = self.content.get_prototype()

    # xmltree.dump(self.xml_root)
    if not as_list:
      if 'CreateSession' in self.node_class.__name__:
        self.content.value = self.xml_root.find('sessionId').text
      else:
        value = self.xml_root.find('value')
        if value:
          for i, argument in enumerate(prototype):
            self.content.value = value[i].text
            self.content.update()
    else:
      self.content.loadxml(self.xml_root)

  def to_json(self): #  -> dict | str
    if not self.content: return ""
    else:
      is_list = is_list_class(self.node_class)
      
      values = self.content.__dict__
      if is_list: 
        values['items'] = [x.attr for x in self.content.items]
      if 'prototype' in values: values.pop('prototype')
      return values

  def __str__(self) -> str:
    return "ApiResponse(status='%s', class='%s')" % (self.status, self.node_class.get_name())

class RadioHttp:
  def __init__(self, host: str, pin: str = RADIO_HTTP_DEFAULT_PIN) -> None:
    self.host = host
    self.pin = pin
    self.sessionid = None
  
  def __str__(self) -> str:
    return "Radio(host='%s', pin='%s')" % (self.host, self.pin)

def is_list_class(node_class) -> bool:
  if type(node_class) != type:
    return False
  for class_name in node_class.__bases__:
    if 'List' in class_name.__name__:
      return True

# [async]
def netremote_request(method: str, node_class, radio: RadioHttp,
                 netconfig: FSNetConfiguration = None, parameters: dict = None) -> ApiResponse:
  node_uri = node_class.get_name()
  if LIST_GET in method: node_uri += '/-l'

  if method not in [GET, LIST_GET_NEXT, SET, LIST_GET]: 
    url = 'http://%s/fsapi/%s?pin=%s' % (radio.host, method, radio.pin) 
  else: 
    url = 'http://%s/fsapi/%s/%s?pin=%s' % (radio.host, method, node_uri, radio.pin)
    if parameters: url += '&' + '&'.join(['%s=%s' % (key, parameters[key]) for key in parameters])

  if netconfig:
    response = netconfig.delegate_request(GET, url)
  else:
    pool = urllib3.PoolManager()
    response = pool.request(GET, url)
  
  if response.status != 200:
    raise NodeError('Invalid response code')
  
  api_response = ApiResponse(node_class)
  api_response.parsexml(response.data, as_list=(LIST_GET in method))
  
  return api_response