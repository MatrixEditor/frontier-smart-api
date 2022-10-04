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
The next module of this small API implementation focusses on the ``FsNetRemoteLib``. 
All nodes that are presented here were converted from the Java-source code of the app 
Medion Lifestream 2. 

The script used for converting the code is placed `here`_. The source code was converted,
because nodes.py contains more that 4000 lines of code in the end (to much work by hand).

When querying a resource or trying to set value to a specific node, there is always a status
message that comes along with the response. The possible values for this status are:

+-------------------------+-------+-----------------------------------------------------------+
| Status                  | Body  | Description                                               |
+=========================+=======+===========================================================+
| `FS_OK`                 | True  | If everything goes right the status is set to `FS_OK`     |
+-------------------------+-------+-----------------------------------------------------------+
| `FS_PACKET_BAD`         | False | This status code will be returned if a value should be    |
|                         |       | applied to a read-only node.                              |
+-------------------------+-------+-----------------------------------------------------------+
| `FS_NODE_BLOCKED`       | False | Sometimes this status is given, maybe because the node    |
|                         |       | was deactivated on the device.                            |
+-------------------------+-------+-----------------------------------------------------------+
|`FS_NODE_DOES_NOT_EXIST` | False | As the name already states, the requested node is not     |
|                         |       | implemented on that device.                               |
+-------------------------+-------+-----------------------------------------------------------+
|`FS_TIMEOUT`             | False | The device takes too long to respond                      |
+-------------------------+-------+-----------------------------------------------------------+ 
| `FS_FAIL`               | False | If the parameters given in the url are mot matching the   |
|                         |       | node criteria, the request will fail.                     |
+-------------------------+-------+-----------------------------------------------------------+
'''

from .basenode import *
from .radiohttp import *
from . import nodes

def get_all_node_names() -> list: # -> list[str]
  '''Returns all loaded node names.'''
  names = []
  for key in nodes.__dict__:
    if 'Base' in key: names.append(nodes.__dict__[key].get_name())
  return names

def get_all_node_types() -> dict: # -> dict[str, type]
  '''Returns all node names together with their class type.
  
  :rtype: dict[str, type]
  '''
  types = {}
  for key in nodes.__dict__:
    if 'Base' in key: 
      class_Type = nodes.__dict__[key]
      types[class_Type.get_name()] = class_Type 
  return types

