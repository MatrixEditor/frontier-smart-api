.. _isuindex:

ISU -- Binary file inspector
================================


**Source code:** `fsapi/isu/__init__.py`_

.. toctree:: 
  :caption: Module Contents:
  :maxdepth: 1

  ioutils
  fsfs
  product

.. raw:: html

   <hr>

.. automodule:: fsapi.isu

All numbers converted from the given buffer will be interpreted as little endian 
encoded numbers as stated in the `firmware analysis`_. 

.. topic:: See also:

    More information about the format numbers are stored in the 
    binary files are given in this `issue <https://github.com/MatrixEditor/frontier-smart-api/issues/3>`_.

Usage
-----

Some usage examples of the ISU module with explainations of each step:

.. code:: python

  # A simple example of how to use the newly added ISUInspector. 
  # 
  # The basic operations of the inspector are:
  #   - get_header
  #   - get_compression_fields
  #   - get_fs_tree
  #   - get_partitions
  from fsapi.isu import *

  # get the inspector instance and load the ISU file
  inspector = ISUInspector.getInstance("ir/mmi/fs2026")
  fp = ISUFile("ir-mmi-FS2026-<file>.isu.bin")

  # load an ISUHeader object and print the loaded data
  header = inspector.get_header(fp, verbose=True)
  print(header)

  # get all partitions and check whether the current 
  # can be interpreted as a web partition
  for partition in inspector.get_partitions(fp, verbose=True):
    if partition.is_web_partition():
      # the return object is an instance of FSFSTree
      tree = inspector.get_fs_tree(fp, verbose=True)
      xml_str =  tree.toXml() 

.. _firmware analysis: https://github.com/MatrixEditor/frontier-smart-api/blob/main/docs/firmware-2.0.md#3-isu-inspector
.. _fsapi/isu/__init__.py: https://github.com/MatrixEditor/frontier-smart-api/blob/main/fsapi/isu/__init__.py