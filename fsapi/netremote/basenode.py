from xml.etree import ElementTree as xmltree

ARG_TYPE_C: int = 0x10
ARG_TYPE_E8: int = 0x11
ARG_TYPE_U8: int = 0x12
ARG_TYPE_U16: int = 0x13
ARG_TYPE_U32: int = 0x14
ARG_TYPE_S8: int = 0x15
ARG_TYPE_S16: int = 0x16
ARG_TYPE_S32: int = 0x17
ARG_TYPE_U: int = 0x18

class NodeArg:
  def __init__(self, name: str = None, length: int = 0, data_type: int = 0) -> None:
    self.name = name
    self.length = length
    self.data_type = data_type

class NodePrototype:
  def __init__(self, arg: NodeArg = None, args: list = None) -> None:
    if arg: self.arguments = [arg]
    elif args: self.arguments = args

  def get_args(self) -> list:
    return self.arguments
  
  def __iter__(self):
    return iter(self.arguments)

class NodeInfo:
  def is_cacheable(self) -> bool:
    return False
  
  def is_notifying(self) -> bool:
    return False

  def is_readonly(self) -> bool:
    return False
  
  def get_name(self) -> str:
    pass

  def get_prototype(self) -> NodePrototype:
    pass

  def update(self):
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
    # if not key: raise error
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