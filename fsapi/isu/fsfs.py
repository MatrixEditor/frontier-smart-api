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
__all__ = [
  'FSFSFile', 'FSFSTree'
]

class FSFSFile:
  def __init__(self, root, tag: str, attributes: dict, text: str = None) -> None:
    self.tag = tag
    self.attr = attributes
    self.root = root
    self.text = text
    self.elements = []

  def get_elements(self) -> list:
    return self.elements

  def get_element(self, tag):
    for elem in self.elements:
      if elem.tag == tag:
        return elem

  def set_attribute(self, name, value):
    if name: self.attr[name] = value

  def get_attribute(self, name):
    if name: return self.attr[name]

  def toXml(self, indent='') -> str:
    txt = self.text if self.text else ""
    xml_str = "%s<%s%s" % (
      indent, self.tag,
      self._attr_to_str()
    )
    if not self.text and len(self.elements) == 0:
      return xml_str + "/>"
    else:
      xml_str += '>'
      if len(self.elements) != 0:
        for element in self.elements:
          xml_str += '\n' + element.toXml(indent=indent + '\t')
      if self.text:
        return xml_str + "%s</%s>" % (txt, self.tag)
      else: 
        return xml_str + "\n%s</%s>" % (indent, self.tag)

  def _attr_to_str(self) -> str:
    if len(self.attr) == 0: 
      return ""
    else:
      x_str = []
      for key in self.attr:
        value = self.attr[key]
        if type(value) == str:
          x_str.append('%s="%s"' % (key, value))
        else:
          x_str.append('%s=%d' % (key, value))
      return ' ' + ', '.join(x_str)
    
  def append(self, e):
    if e: self.get_elements().append(e)
  
  def rem_attribute(self, name):
    if name: self.attr.pop(name)

class FSFSTree(FSFSFile):
  def __init__(self, root: FSFSFile = None, attributes: dict = None) -> None:
    super().__init__(root, 'fsh1', 
      attributes if attributes else {'name': 'Frontier-Silicon-FS'}
    )
