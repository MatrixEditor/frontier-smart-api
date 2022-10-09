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
The ISU module (renamed from 'fisu') now located in the `fsapi` python module
contains an API for inspecting Frontier Smart's update binaries.

By default, update binaries from `mmi` and `cui` interfaces can be inspected by
retrieving their **ISUInspector** instance. Own implementations can be registered 
via calling ``@set_inspector(name)``::

    from fsapi.isu import *
    
    @set_inspector("myname")
    class MyInspector(ISUInspector):
      # ...

Instances of the ``ISUInspector`` should be able to

* read and extract ``ISUHeader`` objects from a given buffer,
* read and extract ``ISUPartition`` objects,
* and optionally read and extract a stored directory archive

Additionally, this module contains a `Tree` implementation in ``FSFSFile`` (Frontier
Smart File System File). It is mainly used to store the extracted data in the XML-
Format. Some usage examples can be viewed in the newer version of the `isu_inspector`
tool. 

The following table shows all top-level names of the ISUInspector class provided in this
API:

+--------+---------------------------------------------------------------------------------+
|  Name  | Description                                                                     |
+========+=================================================================================+
| ir/mmi | Basic ISU inspectors for most of the firmware binaries. All standard operations |
|        | are supported by the returned instance.                                         |       
+--------+---------------------------------------------------------------------------------+
| ir/cui | Inspectors written to handle files from devices with the CUI module type. Only  |
|        | the ``get_header()`` method will work here.                                     |
+--------+---------------------------------------------------------------------------------+
| ns/mmi | These special inspectors will inspect ``ota.bin`` files from devices with the   |
|        | Minuet module. Only the ``get_header()`` and ``get_boot_config()`` method       |
|        | can be called.                                                                  |
+--------+---------------------------------------------------------------------------------+
'''

__version__ = "0.1.8"
__author__ = "MatrixEditor"

from .fsfs import *
from .product import *
from .walk import *
from .inspectors import *

