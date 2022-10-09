.. _ecmascript:

==========================
ECMAScript-Language module
==========================

Note that this module is still under development, so there is no gurantee that methods
will work without any errors. 

.. automodule:: fsapi.ecmascript

.. toctree:: 
  :caption: Module Contents:
  :maxdepth: 1

  esbin

Basic usage (v0.2.0)
~~~~~~~~~~~~~~~~~~~~

.. code:: python

  buffer = ... # es.bin file data
  script = ecmascript.load_rstrings(buffer)

  # iterate over all possible sub-scripts placed in the main script
  for subscript in script:
    # get parsed resource strings (packed into a list)
    rstrings = subscript.components

.. raw:: html

   <hr>

**Source code:** `fsapi/ecmascript/__init__.py`_

.. _fsapi/ecmascript/__init__.py: https://github.com/MatrixEditor/frontier-smart-api/blob/main/fsapi/ecmascript/__init__.py
.. _ecma: https://www.ecma-international.org/publications-and-standards/standards/ecma-262/