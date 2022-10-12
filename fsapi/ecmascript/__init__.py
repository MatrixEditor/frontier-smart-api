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
Products with the `Venice 8` module contain a different directory archive 
structure compared to the common modules `Venice 6` or `Venice X`. This fact is
interesting, because the stored files are mostly graphical resources and script
files written in `ECMAScript` by `ecma`_.

To extract (and uncompress) the stored files, you can use the `isu_inspector`
tool or directly execute the ``fsapi.isu`` module. Files that can be used within
this module end with the ``.es.bin`` suffix (`es` for ecmascript).

Allthough, there is no binary structure definition of ECMAScript files available, 
this module tries to read and extract data from input files. Decompilation of
`.es.bin` files back to ECMAScript code can be a possible feature for future
releases.
'''

from .esbin import *
from .opcode import *