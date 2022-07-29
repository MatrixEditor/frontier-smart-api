import os
import re

from fsapi.netremote.basenode import *

RE_EXTENDS = r"nds [\w<>]* impl"
RE_ENUM = r"enum \w* {(\s*\S*\s*|})"
RE_NAME = r"class \w* e"
RE_IS_CACHEABLE = r"IsCacheable.*\s.*\s.*}"
RE_IS_NOTIFYING = r"IsNotifying.*\s.*\s.*}"
RE_IS_READONLY = r"IsReadOnly.*\s.*\s.*}"
RE_NODE_NAME = r"Name.*\s.*\s.*}"
RE_PROTOTYPE_ARGS = r"Prototype == null(\s*.*\s*|})"

def data_type_from_str(data_type: str) -> int:
  if 'U32' in data_type: return ARG_TYPE_U32
  if 'U16' in data_type: return ARG_TYPE_U16
  if 'U8' in data_type: return ARG_TYPE_U8
  if 'S32' in data_type: return ARG_TYPE_S32
  if 'S16' in data_type: return ARG_TYPE_S16
  if 'S8' in data_type: return ARG_TYPE_S8
  if 'E8' in data_type: return ARG_TYPE_E8
  if 'C8' in data_type: return ARG_TYPE_C


# 'decompiled-app/sources/com/frontier_silicon/NetRemoteLib/Node'
path = input('[~] Path to Node-Classes: ')

_files = []
for _, _, files in os.walk(path):
  _files = files

nodes = []
for _res in _files:
  if 'Base' in _res and _res != 'BaseClasses.java':
    nodes.append(_res) 

print('[+] Found %d nodes...' % len(nodes))
nodes.sort()
txt_elements = {}
for node_file_name in nodes:
  content = open(path + '/' + node_file_name, 'r').read()
  match = re.search(RE_EXTENDS, content)
  ext_class = match.group()[4:-5]
  class_name = re.search(RE_NAME, content).group()[6:-2]

  if 'NodeE8' in ext_class: # enum class type
    enum_type = content[content.find('enum') + 4:]
    enum_type = enum_type[enum_type.find('{'):enum_type.find('}')]
    
    txt = 'class %s(NodeE8):\n  ' % class_name
    txt += 'def __init__(self, value: int = 0) -> None:\n'
    x = enum_type.replace('\n', '').replace('{', '').replace(' ', '').split(',')
    tx_1 = []
    for y in x:
      if y: tx_1.append(y)
    
    txt += '    super().__init__(value, { %s })\n' % (
      ', '.join('%d: "%s"' %(i, val) for i, val in enumerate(tx_1))
    )
    txt += '    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))\n'
    
  elif ext_class in ['NodeList']:
    txt = 'class %s(NodeList):\n  ' % class_name
    txt += 'def __init__(self) -> None:\n'
    txt += '    super().__init__()\n'
    
    prototype = content[content.find('Prototype == null'):]
    prototype = prototype[prototype.find('{')+1:prototype.find('}')].split('\n')
    args = []
    for argument in prototype:
      if 'arrayList.add' not in argument: continue
      name, data_type, length = argument[argument.rfind("(")+1:].split(', ')
      if '"' in name: name = name[1:-1]
      else: name = '$' + name
      length = length[:length.find(')')]
      args.append("NodeArg('%s', %d, %d)" % (
        name, int(length), data_type_from_str(data_type)
      ))
    txt += '    self.prototype = NodePrototype(args=[%s])\n' % (', '.join(args))
  else:
    txt = 'class %s(%s):\n' % (class_name, ext_class)
    txt += '  def __init__(self, value: str = None) -> None:\n'
    txt += '    super().__init__(value, 1024)\n'
    txt += '    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_%s))\n' % (
      ext_class.replace('Node', '')
    )

  cacheable = True if 'true' in re.search(RE_IS_CACHEABLE, content).group() else False
  notifying = True if 'true' in re.search(RE_IS_NOTIFYING, content).group() else False
  readonly = True if 'true' in re.search(RE_IS_READONLY, content).group() else False

  node_name =  re.search(RE_NODE_NAME, content).group()
  node_name = node_name[node_name.find('"')+1:node_name.rfind('"')]

  txt += """
  @staticmethod
  def is_cacheable() -> bool:
    return %s
  
  @staticmethod
  def is_notifying() -> bool:
    return %s

  @staticmethod
  def is_readonly() -> bool:
    return %s
  
  @staticmethod
  def get_name() -> str:
    return '%s'
  
  def get_prototype(self) -> str:
    return self.prototype\n
""" % (cacheable, notifying, readonly, node_name)
  txt_elements[node_name] = txt
  print(txt)

base_path = input('[~] Choose a folder to save the code: ')
with open(base_path + 'nodes.py', 'w') as _res:
  txt = """# This code was generated from JAVA source code
# DO NOT CHANGE\nfrom .basenode import *\n"""
  _res.write(txt)
  for node_name in txt_elements:
    _res.write('\n' + txt_elements[node_name])
    


