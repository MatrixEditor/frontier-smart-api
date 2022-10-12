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

from . import *
from os import walk
from argparse import ArgumentParser

def decompile(dpath: str, fpath: str, opath: str):
  with Decompiler(dpath, fpath) as decompiler:
    code = str(decompiler)
    if opath:
      with open(opath, 'w') as fp:
        fp.write(code)
    else:
      print(code)

def walk_rec(dpath: str, fpath: str):
  for dirpath, dirnames, filenames in walk(fpath):
    for filename in filenames:
      decompile(dpath, dirpath + '/' + filename, dirpath + '/' + filename.replace('es.bin', 'js'))
    for dirname in dirnames:
      walk_rec(dpath, dirpath + '/' + dirname)

if __name__ == '__main__':
  parser = ArgumentParser()

  parser.add_argument('-d', '--decompile', action='store_true', 
    help="Indicates that the given input file should be decompiled."
  )
  parser.add_argument('path', type=str,
    help="The target file that will be used to operate on."
  )
  parser.add_argument('-o', '--out', type=str, default=None,
    help="The path were the decompiled output should be saved."
  )

  group1 = parser.add_argument_group()
  group1.add_argument('--use-decompiler', type=str, metavar='DECOMPATH',
    default='decompiler/ecma-decompiler', help="Specifies the path to the decompiler."
  )
  group1.add_argument('-r', '--recurse', action='store_true',
    help="Indicates that all files in the given directory should be decompiled"
  )
  
  nspace = parser.parse_args().__dict__
  print(nspace)

  if nspace['decompile']:
    fpath = nspace['path']
    dpath = nspace['use_decompiler']
    opath = nspace['out']

    if nspace['recurse']:
      walk_rec(dpath, fpath)
    else:
      decompile(dpath, fpath, opath)
        
  