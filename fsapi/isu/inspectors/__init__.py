
__doc__ = '''
This additional module stores two ``ISUInspector`` implementations that can 
handle ``.ota.bin`` files from `ns-mmi` and ``isu.bin`` files from `ir-mmi`
devices. For more information about the device type and their module type, 
see the ``FSCustomisation`` class.

Because the main system for ``ota.bin`` files is encrypted (or compressed), 
only the header and the U-Boot configuration script can be extracted from 
them. The ``UBootConfig`` can be retrieved via the ``get_boot_config`` in 
the OtaInspector instance.
'''

from .fs2026 import *
from .fs2028 import *
from .fs2340 import *
from .fs5332 import *
