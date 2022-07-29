from .basenode import *
from .radiohttp import *
from . import nodes

def get_all_node_names(): # -> list[str]
  names = []
  for key in nodes.__dict__:
    if 'Base' in key: names.append(nodes.__dict__[key].get_name())
  return names

def get_all_node_types(): # -> dict[str, type]
  types = {}
  for key in nodes.__dict__:
    if 'Base' in key: 
      class_Type = nodes.__dict__[key]
      types[class_Type.get_name()] = class_Type 
  return types

