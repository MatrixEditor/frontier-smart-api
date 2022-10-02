# A simple example of how to use the newly added ISUInspector. By now, only
# the 'mmi' inspector is implemented - 'cui' will be added in the future.
# 
# The basic operations of th inspector are:
#   - get_header
#   - get_compression_fields
#   - get_fs_tree
from fsapi.isu import *

# get the inspector instance and load the ISU file
inspector = ISUInspector.getInstance("mmi")
fp = ISUFile("ir-mmi-<file>.isu.bin")

# load an ISUHeader object and print the loaded data
header = inspector.get_header(fp, verbose=True)
print(header)
