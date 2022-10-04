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
Basic network operations on the NetRemote API will be delegated via the 
``netremote_request()`` method. For all operations done in this small API, the 
``RadioHttp`` class is used, even if it's a small wrapper class.

'''

import urllib3
import xml.etree.ElementTree as xmltree

from ..netconfig import FSNetConfiguration

__all__ = [ 
  "RADIO_HTTP_DEFAULT_PIN", "GET", "GET_MULTIPLE", "SET", "SET_MULTIPLE", 
  "LIST_GET", "LIST_GET_NEXT", "CREATE_SESSION", "DELETE_SESSION",
  "NodeError", "ApiResponse", "RadioHttp", "netremote_request",
  "is_list_class"
]

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
  """The base class for all node related issues."""
  pass

class ApiResponse:
  '''An object wrapper storing HTTP response data.
  
  :param node_class: the result type
  :param xml_root: the root element of the XML-response
  :param content: a node instance of type ``node_class``, which is created when 
                  ``parsexml()`` was called.
  :param status: the status code from the HTTP-response
  '''
  
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
  '''A simple storage object containing the radio's ip-address and pin.
  
  :param host: the target host IP-Address.
  :param pin: the target's PIN (default "`1234`"). 
  '''
  def __init__(self, host: str, pin: str = RADIO_HTTP_DEFAULT_PIN) -> None:
    self.host = host
    self.pin = pin
    self.sessionid = None
  
  def __str__(self) -> str:
    return "Radio(host='%s', pin='%s')" % (self.host, self.pin)

def is_list_class(node_class) -> bool:
  '''Returns whether the given node class has ``NodeList`` as its base class.'''
  if type(node_class) != type:
    return False
  for class_name in node_class.__bases__:
    if 'List' in class_name.__name__:
      return True

# [async]
def netremote_request(method: str, node_class, radio: RadioHttp,
                 netconfig: FSNetConfiguration = None, parameters: dict = None) -> ApiResponse:
  '''Performs a NetRemote-Request.

  This method can be called in different situations and will behave always the same: First, it 
  creates the URL to be called. Next, the result of that call will be converted into an 
  ``ApiResponse`` object. 

  It can be used as follows:

  >>> radio = RadioHttp('127.0.0.1')
  >>> fsapi.netremote_request('SET', fsapi.nodes.BaseSysInfoFriendlyName, radio, parameters={'value': "Hello World"})
  ApiResponse(status='200', class='BaseSysInfoFriendlyName')
  >>> result = fsapi.netremote_request('GET', fsapi.nodes.BaseSysInfoFriendlyName, $radio)
  >>> result.content.value
  Hello World

  :param method: the dedicated method to use (one of the following: `GET`, `SET`, `LIST_GET_NEXT`, 
                 `CREATE_SESSION`). `GET_MULTIPLE` and `SET_MUTLIPLE` are not supported yet.
  :param node_class: the class type of the node which will be queried
  :param radio: the radio object storing the pin value and the target host string
  :param netconfig: if a custom configuration like a proxy should be used, this object can be passed as a 
                    parameter.
  :param parameters: used if a list of items is queried or a new value should be applied to a node. Please 
                     refer to the related node class, which parameters are accepted (if there is no argument
                     name, use value as parameter name).
  
  :returns: an ``ApiReponse`` object including a node instance with the gathered value
  '''

  node_uri = node_class.get_name()
  if LIST_GET in method: node_uri += '/-l' # -l for -list

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