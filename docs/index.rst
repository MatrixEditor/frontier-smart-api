.. frontier-smart-api documentation master file, created by
   sphinx-quickstart on Mon Oct  3 08:55:07 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to frontier-smart-api's documentation!
==============================================

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   api/index

This API Implementation includes all possible Nodes that can be interacted with. Additionally, 
the API comes with a module called isudata to use the backend service by the update-file provider. 

The most important information: Are there any dependencies? - No, besides ``urllib3``, which 
should be installed by default, everything can be used without downloading extra dependencies.

Basic usage
-----------

.. code:: python

   # FSAPI
   import fsapi.all as fsapi

   # 1.Find and download updates
   # without custom netconfig -> HTTPS traffic
   response = fsapi.isu_find_update('$MAC', '$CUSTOM', '$VERSION')

   # with custom config -> force HTTP traffic
   config = fsapi.FSNetConfiguration(http_pool=urllib3.HTTPConnectionPool('$HOST'))
   response = fsapi.isu_find_update('$MAC', '$CUSTOM', '$VERSION', netconfig=config)
   
   # without custom netconfig -> HTTPS traffic
   response = fsapi.isu_find_update('$MAC', '$CUSTOM', '$VERSION')
   for _software in response['updates']:
      fsapi.isu_get_update('$FILE_PATH', software=_software)

   # SET request
   result = fsapi.netremote_request('SET', fsapi.nodes.BaseSysInfoFriendlyName, radio, parameters={'value': "Hello World"})

   # GET request
   result = fsapi.netremote_request('GET', fsapi.nodes.BaseSysInfoFriendlyName, radio)

   # LIST_GET_NEXT request
   result = fsapi.netremote_request('LIST_GET_NEXT', node_class, radio, parameters={'maxItems': 100})

   # ISU
   from fsapi.isu import *

   # get the inspector instance and load the ISU file
   inspector = ISUInspector.getInstance("mmi")
   fp = ISUFile("ir-mmi-<file>.isu.bin")

   # load an ISUHeader object and print the loaded data
   header = inspector.get_header(fp, verbose=True)
   print(header)




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
