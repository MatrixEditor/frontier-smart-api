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
The first two classes are used to add a prototype template to each node. By adding 
a ``NodeArg`` to a ``NodePrototype`` object, the same parameter has to be specified 
when calling the ``netremote_request('SET', ...)`` method. A small example should 
show the importance::

    # <in specific Node class> -> do not change this code 
    # Creating a prototype for the default parameter 'value' of type ui16.
    prototype = NodePrototype(arg=NodeArg(data_Type=ARG_TYPE_U16))

    # <custom code>
    # If calling the SET method, the parameter has to be given
    result = fsapi.netremote_request('SET', $node_class, $radio, parameters={'value': 1})

There are only a few `ARG_TYPE` values implemented and possible to use. These are:

* ``ARG_TYPE_C``:   int = 0x10  # C8-Array (char array) 
* ``ARG_TYPE_E8``:  int = 0x11  # Type defined by an Enum
* ``ARG_TYPE_U8``:  int = 0x12  # unsigned char
* ``ARG_TYPE_U16``: int = 0x13  # unsigned short
* ``ARG_TYPE_U32``: int = 0x14  # unsigned int
* ``ARG_TYPE_S8``:  int = 0x15  # signed char
* ``ARG_TYPE_S16``: int = 0x16  # signed short
* ``ARG_TYPE_S32``: int = 0x17  # signed int
* ``ARG_TYPE_U``:   int = 0x18  # array of data

The node classes represent the base of all possible functionalities this API provides. The 
package name of each node class can be fetched by calling the static method ``node_class.get_name()``.
Use ``fsapi.get_all_node_names()`` to get all implemented nodes.

Each node provides the following attributes: ``cacheable`` [bool], ``notifying`` [bool], 
``readonly`` [bool], <static> ``package_name`` [str], ``prototype`` [NodePrototype] and the 
stored value in case the node is not a ``NodeList``. These node list classes just contain a list 
of ``NodeListItems``, which can contain one ore more fields. These are packed into a dictionary 
named `attr`.

To make the import of NodeLists and NodeListItems easier, these classes come with an inbuild function 
named ``loadxml()``. Note that the XMLElement always needs to be the root element.
'''

from xml.etree import ElementTree as xmltree

__all__ = [
"ARG_TYPE_C", "ARG_TYPE_E8", "ARG_TYPE_U8", "ARG_TYPE_U16", "ARG_TYPE_U32", "ARG_TYPE_S8", 
"ARG_TYPE_S16", "ARG_TYPE_S32", "ARG_TYPE_U", "NodeArg", "NodePrototype", "NodeInfo", 
"NodeInteger", "NodeS8", "NodeS16", "NodeS32", "NodeU8", "NodeU16", "NodeU32", "NodeE8",
"NodeC", "NodeU", "NodeListItem", "NodeList", 
]

ARG_TYPE_C: int = 0x10
'''C8-Array (char array)'''
ARG_TYPE_E8: int = 0x11
'''Type defined by an Enum'''
ARG_TYPE_U8: int = 0x12
'''unsigned char'''
ARG_TYPE_U16: int = 0x13
'''unsigned short'''
ARG_TYPE_U32: int = 0x14
'''unsigned int'''
ARG_TYPE_S8: int = 0x15
'''signed char'''
ARG_TYPE_S16: int = 0x16
'''signed short'''
ARG_TYPE_S32: int = 0x17
'''signed int'''
ARG_TYPE_U: int = 0x18
'''array of data'''

class NodeArg:
  '''A simple Node-Argument.
  
  This class has to be added to the ``NodePrototype`` if the node can be altered. The
  default name for an argument is "`value`".

  :param name: the argument's name (default "`value`")
  :param length: the maximum data length
  :param data_type: one of the previous declared data types
  '''
  def __init__(self, name: str = None, length: int = 0, data_type: int = 0) -> None:
    self.name = name
    self.length = length
    self.data_type = data_type

class NodePrototype:
  '''The prototype for a node definition. 
  
  This class stores the arguments that are necessary when reading from or writing to 
  a node.

  :param arg: a single ``NodeArg``
  :param args: a list of ``NodeArg``
  '''
  
  def __init__(self, arg: NodeArg = None, args: list = None) -> None:
    if arg: self.arguments = [arg]
    elif args: self.arguments = args if args else []

  def get_args(self) -> list:
    '''Returns the stored node's arguments.'''
    return self.arguments
  
  def __iter__(self):
    return iter(self.arguments)

class NodeInfo:
  '''The base class for all nodes.
  
  As defined above, each node provides the following attributes: ``cacheable`` [bool], 
  ``notifying`` [bool], ``readonly`` [bool], <static> ``package_name`` [str], ``prototype`` 
  [NodePrototype] and the stored value in case the node is not a ``NodeList``.
  '''

  def is_cacheable(self) -> bool:
    '''Returns whether this node can be cached (on the device).'''
    return False
  
  def is_notifying(self) -> bool:
    '''Returns whether this node is notifying.'''
    return False

  def is_readonly(self) -> bool:
    '''Returns whether this node can't be altered.'''
    return False
  
  def get_name(self) -> str:
    '''Returns the name of this node.'''
    pass

  def get_prototype(self) -> NodePrototype:
    '''Returns the prototype for this node.'''
    pass

  def update(self):
    '''@Deprecated'''
    pass

class NodeInteger(NodeInfo):
  def __init__(self, value: int, min_value: int = 0, max_value: int = 0) -> None:
    self.value = value
    self.minimum = min_value
    self.maximum = max_value
  
  def get_value(self) -> int:
    return self.value

  def update(self):
    if type(self.value) == str:
      self.value = int(self.value)
  
  def __str__(self) -> str:
    return "NodeInt(v=%s)" % str(self.get_value())

  def __eq__(self, __o: object) -> bool:
    if type(__o) == self.__class__:
      return __o.get_value() == self.get_value() 

class NodeS8(NodeInteger):
  def __init__(self, value: int, max_size: int = 0) -> None:
    super().__init__(value, 127, -127)

class NodeS16(NodeInteger):
  def __init__(self, value: int, max_size: int = 0) -> None:
    super().__init__(value, 0x7fff, -0x7fff)

class NodeS32(NodeInteger):
  def __init__(self, value: int, max_size: int = 0) -> None:
    super().__init__(value, 0x7fffffff, -0x7fffffff)

class NodeU8(NodeInteger):
  def __init__(self, value: int, max_size: int = 0) -> None:
    super().__init__(value, 0xff, 0)

class NodeU16(NodeInteger):
  def __init__(self, value: int, max_size: int = 0) -> None:
    super().__init__(value, 0xffff, 0)

class NodeU32(NodeInteger):
  def __init__(self, value: int, max_size: int = 0) -> None:
    super().__init__(value, 0xffffffff, 0)

class NodeE8(NodeInfo):
  def __init__(self, value: int = 0, mapping: dict = None) -> None:
    self.value = value
    self.mapping = mapping

  def get_enum_value(self) -> object:
    if not self.mapping or self.value not in self.mapping: return None
    return self.mapping[self.value]

  def get_value(self) -> int:
    return self.value

  def __str__(self) -> str:
    return 'NodeE8<%s>' % self.get_enum_value()

class NodeC(NodeInfo):
  def __init__(self, value: str = None, max_size: int = 0) -> None:
    super().__init__()
    self.value = value
    self.max_size = max_size
  
  def get_maximum_length(self) -> int:
    return self.max_size

class NodeU(NodeC):
  def __init__(self, value: str = None, max_size: int = 0) -> None:
    super().__init__(value, max_size)

class NodeListItem:
  def __init__(self, attributes: dict = None) -> None:
    self.attr = attributes if attributes else {}

  def loadxml(self, element: xmltree.Element):
    key = element.get('key', None)
    self.attr['key'] = key
    for field_node in element.findall('field'):
      self.attr[field_node.attrib['name']] = field_node[0].text
  
  def get_attr_by_name(self, field: str) -> object:
    if not field or field not in self.attr: return None
    return self.attr[field]

class NodeList(NodeInfo):
  def __init__(self, items: list = None) -> None:
    super().__init__()
    self.items = items if items else []

  def loadxml(self, element: xmltree.Element):
    for item in element.findall('item'):
      node_item = NodeListItem()
      node_item.loadxml(item)
      self.get_items().append(node_item)

  def size(self) -> int:
    return len(self.items)
  
  def get_items(self) -> list:
    return self.items