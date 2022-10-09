.. _esbin:

==================================
ECMAScript binary inspector/parser
==================================

.. automodule:: fsapi.ecmascript.esbin

.. autoattribute:: fsapi.ecmascript.esbin.ES_BIN_SUFFIX

This module will accept files with an extension that matches this defined
regular expression. The following examples should show which file names 
are included:

>>> esbin.is_valid_ext('foobar.es.bin')
True
>>> esbin.is_valid_ext('foobar.es')
False
>>> esbin.is_valid_ext('foobar.es6.bin')
True

.. autoattribute:: fsapi.ecmascript.esbin.ES_BIN_MAGIC

ECMAScript binary files always start with header information and a file 
signature, which is ``07 00 AD DE``.

.. autofunction:: is_valid_ext

.. autofunction:: read_rstring

.. autofunction:: load_rstrings

.. autoclass:: ECMAScriptHeader
  :members:

.. autoclass:: ECMAScript
  :members:
