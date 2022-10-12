.. _esbin:

============================
ECMAScript binary decompiler
============================

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
signature, which is ``DE AD 00 07`` (ScriptMonkey v1.8).

.. autofunction:: is_valid_ext

.. autoclass:: Decompiler
  :members:
