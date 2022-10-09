# This code was generated from JAVA source code
# DO NOT CHANGE
from .basenode import *

class BaseCreateSession(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)

  @staticmethod
  def get_name() -> str:
    return 'CREATE_SESSION'
  
class BaseAirplayClearPassword(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "CLEAR" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.airplay.clearPassword'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseAirplaySetPassword(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.airplay.setPassword'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseAvsAlarmVolume(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.avs.alarmVolume'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseAvsAuthcode(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.avs.authcode'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseAvsHastoken(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "FALSE", 1: "TRUE" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.avs.hastoken'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseAvsLocale(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.avs.locale'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseAvsLogout(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.avs.logout'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseAvsMetadata(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.avs.metadata'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseAvsProductmetadata(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.avs.productmetadata'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseAvsToken(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.avs.token'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseAvsValidLocales(NodeList):
  def __init__(self) -> None:
    super().__init__()
    self.prototype = NodePrototype(args=[NodeArg('key', 1, 20), NodeArg('name', 50, 16), NodeArg('code', 20, 16)])

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.avs.validLocales'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseBluetoothConnectedDevices(NodeList):
  def __init__(self) -> None:
    super().__init__()
    self.prototype = NodePrototype(args=[NodeArg('key', 1, 20), NodeArg('deviceState', 1, 17), NodeArg('deviceName', 65, 16)])

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.bluetooth.connectedDevices'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseBluetoothConnectedDevicesListVersion(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.bluetooth.connectedDevicesListVersion'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseBluetoothDiscoverableState(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "IDLE", 1: "DISCOVERABLE" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.bluetooth.discoverableState'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseCastAppName(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.cast.appName'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseCastTos(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "INACTIVE", 1: "ACTIVE", 2: "UNSET" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.cast.tos'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseCastUsageReport(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "INACTIVE", 1: "ACTIVE" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.cast.usageReport'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseCastVersion(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.cast.version'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseFsdcaAuthCode(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.fsdca.authCode'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseFsdcaClientId(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.fsdca.clientId'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseFsdcaDisassociate(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "NO_REQUEST", 1: "DISSASOCIATE" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.fsdca.disassociate'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseFsdcaFsdcaId(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.fsdca.fsdcaId'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseFsdcaState(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "FSDCA_STATE_INITIAL", 1: "FSDCA_STATE_NOT_ASSOCIATED", 2: "FSDCA_STATE_AUTH_IN_PROGRESS", 3: "FSDCA_STATE_CONNECTING", 4: "FSDCA_STATE_CONNECTED", 5: "FSDCA_STATE_WAITING" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.fsdca.state'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMiscFsDebugComponent(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.misc.fsDebug.component'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMiscFsDebugTraceLevel(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.misc.fsDebug.traceLevel'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseDebugIncidentReportLastCreatedKey(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.debug.incidentReport.lastCreatedKey'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseDebugIncidentReportCreate(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.debug.incidentReport.create'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseDebugIncidentReportList(NodeList):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(args=[
      NodeArg('uuid', 100, ARG_TYPE_C), NodeArg('path', 100, ARG_TYPE_C),
      NodeArg('time', 100, ARG_TYPE_C), NodeArg('key', 100, ARG_TYPE_C)
    ])

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.debug.incidentReport.list'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseDebugIncidentReportDelete(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.debug.incidentReport.delete'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMiscNvsData(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.misc.nvs.data'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultichannelPrimaryChannelmask(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "NONE", 1: "LEFT", 2: "RIGHT", 3: "STEREO" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multichannel.primary.channelmask'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultichannelSecondary0Channelmask(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "NONE", 1: "LEFT", 2: "RIGHT", 3: "STEREO" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multichannel.secondary0.channelmask'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultichannelSecondary0Status(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "SYNCHRONISING", 1: "READY", 2: "INVALID" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multichannel.secondary0.status'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultichannelSystemAddsecondary(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multichannel.system.addsecondary'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultichannelSystemCompatibilityid(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multichannel.system.compatibilityid'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultichannelSystemCreate(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multichannel.system.create'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultichannelSystemId(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multichannel.system.id'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultichannelSystemName(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multichannel.system.name'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultichannelSystemRemovesecondary(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multichannel.system.removesecondary'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultichannelSystemState(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "INDEPENDENT", 1: "PRIMARY", 2: "SECONDARY" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multichannel.system.state'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultichannelSystemUnpair(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "IDLE", 1: "UNPAIR" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multichannel.system.unpair'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomCapsMaxClients(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.caps.maxClients'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomCapsProtocolVersion(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.caps.protocolVersion'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomClientMute0(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "NOT_MUTE", 1: "MUTE" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.client.mute0'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomClientMute1(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "NOT_MUTE", 1: "MUTE" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.client.mute1'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomClientMute2(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "NOT_MUTE", 1: "MUTE" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.client.mute2'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomClientMute3(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "NOT_MUTE", 1: "MUTE" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.client.mute3'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomClientStatus0(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "CONNECTED", 1: "SYNCRONIZING", 2: "READY_TO_STREAM" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.client.status0'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomClientStatus1(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "CONNECTED", 1: "SYNCRONIZING", 2: "READY_TO_STREAM" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.client.status1'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomClientStatus2(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "CONNECTED", 1: "SYNCRONIZING", 2: "READY_TO_STREAM" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.client.status2'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomClientStatus3(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "CONNECTED", 1: "SYNCRONIZING", 2: "READY_TO_STREAM" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.client.status3'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomClientVolume0(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.client.volume0'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomClientVolume1(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.client.volume1'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomClientVolume2(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.client.volume2'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomClientVolume3(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.client.volume3'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomDeviceClientIndex(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.device.clientIndex'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomDeviceClientStatus(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "CONNECTED", 1: "SYNCRONIZING", 2: "READY_TO_STREAM" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.device.clientStatus'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomDeviceListAll(NodeList):
  def __init__(self) -> None:
    super().__init__()
    self.prototype = NodePrototype(args=[NodeArg('key', 1, 20), NodeArg('UDN', 256, 16), NodeArg('FriendlyName', 256, 16), NodeArg('IPAddress', 16, 16), NodeArg('AudioSyncVersion', 11, 16), NodeArg('GroupId', 37, 16), NodeArg('GroupName', 256, 16), NodeArg('GroupRole', 1, 17), NodeArg('ClientNumber', 1, 18), NodeArg('SystemId', 37, 16), NodeArg('SystemRole', 1, 17), NodeArg('SystemName', 256, 16)])

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.device.listAll'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomDeviceListAllVersion(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.device.listAllVersion'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomDeviceServerStatus(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "STREAM_STARTING", 1: "STREAM_PRESENTABLE", 2: "STREAM_UNPRESENTABLE" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.device.serverStatus'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomDeviceTransportOptimisation(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "DISABLED", 1: "ENABLED" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.device.transportOptimisation'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomGroupAddClient(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.group.addClient'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomGroupAttachedClients(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.group.attachedClients'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomGroupBecomeServer(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "NO_GROUP", 1: "CLIENT", 2: "SERVER" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.group.becomeServer'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomGroupCreate(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.group.create'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomGroupDestroy(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "IDLE", 1: "DESTROY" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.group.destroy'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomGroupId(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.group.id'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomGroupMasterVolume(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.group.masterVolume'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomGroupName(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.group.name'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomGroupRemoveClient(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.group.removeClient'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomGroupState(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "NO_GROUP", 1: "CLIENT", 2: "SERVER" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.group.state'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomGroupStreamable(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "FALSE", 1: "TRUE" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.group.streamable'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseMultiroomSinglegroupState(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "SINGLE", 1: "MULTIROOM" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.multiroom.singlegroup.state'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavActionContext(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.action.context'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavActionDabPrune(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "IDLE", 1: "PRUNE" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.action.dabPrune'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavActionDabScan(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "IDLE", 1: "SCAN" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.action.dabScan'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavActionNavigate(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.action.navigate'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavActionSelectItem(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.action.selectItem'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavActionSelectPreset(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.action.selectPreset'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavAmazonMpGetRating(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.amazonMpGetRating'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavAmazonMpLoginComplete(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "FALSE", 1: "TRUE" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.amazonMpLoginComplete'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavAmazonMpLoginUrl(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.amazonMpLoginUrl'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavAmazonMpSetRating(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "POSITIVE", 1: "NEGATIVE" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.amazonMpSetRating'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavBrowseMode(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.browseMode'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavCaps(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.caps'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavContextDepth(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.context.depth'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavContextErrorStr(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.context.errorStr'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavContextFormData(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.context.formData'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavContextFormItem(NodeList):
  def __init__(self) -> None:
    super().__init__()
    self.prototype = NodePrototype(args=[NodeArg('key', 1, 20), NodeArg('formItemType', 1, 17), NodeArg('id', 32, 16), NodeArg('label', 32, 16), NodeArg('description', 256, 16), NodeArg('optionsCount', 1, 19)])

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.context.form.item'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavContextFormOption(NodeList):
  def __init__(self) -> None:
    super().__init__()
    self.prototype = NodePrototype(args=[NodeArg('key', 1, 20), NodeArg('name', 32, 16)])

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.context.form.option'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavContextList(NodeList):
  def __init__(self) -> None:
    super().__init__()
    self.prototype = NodePrototype(args=[NodeArg('key', 1, 20), NodeArg('name', 766, 16), NodeArg('type', 1, 17), NodeArg('subType', 1, 17)])

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.context.list'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavContextNavigate(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.context.navigate'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavContextNumItems(NodeS32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_S32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.context.numItems'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavContextRefresh(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "FALSE", 1: "TRUE" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.context.refresh'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavContextStatus(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "WAITING", 1: "READY", 2: "FAIL", 3: "FATAL_ERR", 4: "READY_ROOT" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.context.status'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavCurrentTitle(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.currentTitle'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavDabScanUpdate(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.dabScanUpdate'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavDepth(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.depth'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavDescription(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.description'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavEncFormData(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.encFormData'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavErrorStr(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.errorStr'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavFormButton(NodeList):
  def __init__(self) -> None:
    super().__init__()
    self.prototype = NodePrototype(args=[NodeArg('key', 1, 20), NodeArg('name', 32, 16)])

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.form.button'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavFormData(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.formData'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavFormItem(NodeList):
  def __init__(self) -> None:
    super().__init__()
    self.prototype = NodePrototype(args=[NodeArg('key', 1, 20), NodeArg('formItemType', 1, 17), NodeArg('id', 32, 16), NodeArg('label', 32, 16), NodeArg('description', 256, 16), NodeArg('optionsCount', 1, 19)])

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.form.item'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavFormOption(NodeList):
  def __init__(self) -> None:
    super().__init__()
    self.prototype = NodePrototype(args=[NodeArg('key', 1, 20), NodeArg('name', 32, 16)])

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.form.option'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavList(NodeList):
  def __init__(self) -> None:
    super().__init__()
    self.prototype = NodePrototype(args=[NodeArg('key', 1, 20), NodeArg('name', 766, 16), NodeArg('type', 1, 17), NodeArg('subType', 1, 17), NodeArg('graphicUri', 766, 16), NodeArg('artist', 766, 16), NodeArg('contextMenu', 1, 17)])

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.list'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavNumItems(NodeS32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_S32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.numItems'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavPresetCurrentPreset(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.preset.currentPreset'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavPresetDelete(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.preset.delete'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavPresetDownloadArtworkUrl(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.preset.download.artworkUrl'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavPresetDownloadBlob(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.preset.download.blob'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavPresetDownloadDownload(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.preset.download.download'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavPresetDownloadName(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.preset.download.name'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavPresetDownloadType(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.preset.download.type'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavPresetListversion(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.preset.listversion'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavPresetSwapIndex1(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.preset.swap.index1'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavPresetSwapIndex2(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.preset.swap.index2'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavPresetSwapSwap(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.preset.swap.swap'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavPresetUploadArtworkUrl(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.preset.upload.artworkUrl'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavPresetUploadBlob(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.preset.upload.blob'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavPresetUploadName(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.preset.upload.name'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavPresetUploadType(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.preset.upload.type'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavPresetUploadUpload(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.preset.upload.upload'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavPresets(NodeList):
  def __init__(self) -> None:
    super().__init__()
    self.prototype = NodePrototype(args=[NodeArg('key', 1, 20), NodeArg('name', 65, 16), NodeArg('type', 32, 16), NodeArg('uniqid', 32, 16), NodeArg('blob', 2064, 16), NodeArg('artworkUrl', 512, 16)])

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.presets'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavRefresh(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "FALSE", 1: "TRUE" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.refresh'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavReleaseDate(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.releaseDate'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavSearchTerm(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.searchTerm'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavState(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "OFF", 1: "ON" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.state'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseNavStatus(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "WAITING", 1: "READY", 2: "FAIL", 3: "FATAL_ERR", 4: "READY_ROOT" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.nav.status'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlatformOEMColorProduct(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.platform.OEM.colorProduct'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlatformOEMLedIntensity(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.platform.OEM.ledIntensity'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlatformOEMLedIntensitySteps(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.platform.OEM.ledIntensitySteps'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlatformSoftApUpdateUpdateModeRequest(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "IDLE", 1: "START" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.platform.softApUpdate.updateModeRequest'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlatformSoftApUpdateUpdateModeStatus(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "IDLE", 1: "STARTED" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.platform.softApUpdate.updateModeStatus'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayAddPreset(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.addPreset'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayAddPresetStatus(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "PRESET_STORRED", 1: "PRESET_NOT_STORRED" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.addPresetStatus'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayAlerttone(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "IDLE", 1: "PLAY" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.alerttone'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayCaps(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.caps'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayConcurencyResponse(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "FALSE", 1: "TRUE" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.ConcurencyResponse'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayConcurencyStr(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.ConcurencyStr'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayControl(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "STOP", 1: "PLAY", 2: "PAUSE", 3: "NEXT", 4: "PREVIOUS" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.control'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayErrorStr(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.errorStr'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayFeedback(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "IDLE", 1: "POSITIVE", 2: "NEGATIVE" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.feedback'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayFrequency(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.frequency'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayInfoAlbum(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.info.album'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayInfoAlbumDescription(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.info.albumDescription'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayInfoArtist(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.info.artist'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayInfoArtistDescription(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.info.artistDescription'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayInfoDescription(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.info.description'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayInfoDuration(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.info.duration'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayInfoGraphicUri(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.info.graphicUri'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayInfoName(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.info.name'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayInfoProviderLogoUri(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.info.providerLogoUri'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayInfoProviderName(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.info.providerName'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayInfoText(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.info.text'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayNotificationMessage(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.NotificationMessage'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayPosition(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.position'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayRate(NodeS8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_S8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.rate'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayRating(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "NEUTRAL", 1: "POSITIVE", 2: "NEGATIVE" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.rating'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayRepeat(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "OFF", 1: "REPEAT_ALL", 2: "REPEAT_ONE" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.repeat'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayScrobble(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "OFF", 1: "ON" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.scrobble'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayServiceIdsDabEnsembleId(NodeU16):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U16))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.serviceIds.dabEnsembleId'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayServiceIdsDabScids(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.serviceIds.dabScids'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayServiceIdsDabServiceId(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.serviceIds.dabServiceId'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayServiceIdsEcc(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.serviceIds.ecc'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayServiceIdsFmRdsPi(NodeU16):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U16))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.serviceIds.fmRdsPi'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayShuffle(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "OFF", 1: "ON" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.shuffle'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayShuffleStatus(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "OK", 1: "SHUFFLING", 2: "TOO_MANY_ITEMS", 3: "UNSUPPORTED" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.shuffleStatus'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlaySignalStrength(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.signalStrength'
  
  def get_prototype(self) -> str:
    return self.prototype

class BasePlayStatus(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "IDLE", 1: "BUFFERING", 2: "PLAYING", 3: "PAUSED", 4: "REBUFFERING", 5: "ERROR", 6: "STOPPED", 7: "ERROR_POPUP" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.play.status'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSpotifyBitRate(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.spotify.bitRate'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSpotifyLastError(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.spotify.lastError'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSpotifyLoggedInState(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "NOT_LOGGED_IN", 1: "LOGGED_IN" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.spotify.loggedInState'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSpotifyLoginUsingOauthToken(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.spotify.loginUsingOauthToken'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSpotifyPlaylistName(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.spotify.playlist.name'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSpotifyPlaylistUri(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.spotify.playlist.uri'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSpotifyStatus(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.spotify.status'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSpotifyUsername(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.spotify.username'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysAlarmConfig(NodeList):
  def __init__(self) -> None:
    super().__init__()
    self.prototype = NodePrototype(args=[NodeArg('key', 1, 20), NodeArg('on', 1, 17), NodeArg('time', 7, 16), NodeArg('duration', 1, 18), NodeArg('source', 1, 17), NodeArg('preset', 1, 18), NodeArg('repeat', 1, 17), NodeArg('date', 9, 16), NodeArg('volume', 1, 18)])

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.alarm.config'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysAlarmConfigChanged(NodeS8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_S8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.alarm.configChanged'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysAlarmCurrent(NodeS8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_S8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.alarm.current'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysAlarmDuration(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.alarm.duration'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysAlarmSnooze(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.alarm.snooze'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysAlarmSnoozing(NodeU16):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U16))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.alarm.snoozing'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysAlarmStatus(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "IDLE", 1: "ALARMING", 2: "SNOOZING" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.alarm.status'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysAudioAirableQuality(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "LOW", 1: "NORMAL", 2: "HIGH" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.audio.airableQuality'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysAudioEqCustomParam0(NodeS16):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_S16))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.audio.eqCustom.param0'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysAudioEqCustomParam1(NodeS16):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_S16))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.audio.eqCustom.param1'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysAudioEqCustomParam2(NodeS16):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_S16))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.audio.eqCustom.param2'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysAudioEqCustomParam3(NodeS16):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_S16))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.audio.eqCustom.param3'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysAudioEqCustomParam4(NodeS16):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_S16))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.audio.eqCustom.param4'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysAudioEqLoudness(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "OFF", 1: "ON" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.audio.eqLoudness'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysAudioEqPreset(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.audio.eqPreset'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysAudioExtStaticDelay(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.audio.extStaticDelay'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysAudioMute(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "NOT_MUTE", 1: "MUTE" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.audio.mute'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysAudioVolume(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.audio.volume'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysCapsClockSourceList(NodeList):
  def __init__(self) -> None:
    super().__init__()
    self.prototype = NodePrototype(args=[NodeArg('key', 1, 20), NodeArg('source', 10, 16)])

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.caps.clockSourceList'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysCapsDabFreqList(NodeList):
  def __init__(self) -> None:
    super().__init__()
    self.prototype = NodePrototype(args=[NodeArg('key', 1, 20), NodeArg('freq', 1, 20), NodeArg('label', 8, 16)])

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.caps.dabFreqList'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysCapsEqBands(NodeList):
  def __init__(self) -> None:
    super().__init__()
    self.prototype = NodePrototype(args=[NodeArg('key', 1, 20), NodeArg('label', 32, 16), NodeArg('min', 1, 22), NodeArg('max', 1, 22)])

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.caps.eqBands'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysCapsEqPresets(NodeList):
  def __init__(self) -> None:
    super().__init__()
    self.prototype = NodePrototype(args=[NodeArg('key', 1, 20), NodeArg('label', 32, 16)])

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.caps.eqPresets'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysCapsExtStaticDelayMax(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.caps.extStaticDelayMax'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysCapsFmFreqRangeLower(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.caps.fmFreqRange.lower'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysCapsFmFreqRangeStepSize(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.caps.fmFreqRange.stepSize'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysCapsFmFreqRangeUpper(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.caps.fmFreqRange.upper'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysCapsFsdca(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.caps.fsdca'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysCapsUtcSettingsList(NodeList):
  def __init__(self) -> None:
    super().__init__()
    self.prototype = NodePrototype(args=[NodeArg('key', 1, 20), NodeArg('time', 1, 23), NodeArg('region', 32, 16)])

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.caps.utcSettingsList'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysCapsValidLang(NodeList):
  def __init__(self) -> None:
    super().__init__()
    self.prototype = NodePrototype(args=[NodeArg('key', 1, 20), NodeArg('langLabel', 32, 16)])

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.caps.validLang'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysCapsValidModes(NodeList):
  def __init__(self) -> None:
    super().__init__()
    self.prototype = NodePrototype(args=[NodeArg('key', 1, 20), NodeArg('id', 8, 16), NodeArg('selectable', 1, 17), NodeArg('label', 32, 16), NodeArg('streamable', 1, 17), NodeArg('modeType', 1, 17)])

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.caps.validModes'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysCapsVolumeSteps(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.caps.volumeSteps'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysCfgIrAutoPlayFlag(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "AUTOPLAY_ON", 1: "AUTOPLAY_OFF" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.cfg.irAutoPlayFlag'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysClockDateFormat(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "DATE_DD_MM_YYYY", 1: "DATE_MM_DD_YYYY" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.clock.dateFormat'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysClockDst(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "OFF", 1: "ON" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.clock.dst'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysClockLocalDate(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.clock.localDate'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysClockLocalTime(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.clock.localTime'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysClockMode(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "_12_HOUR", 1: "_24_HOUR" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.clock.mode'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysClockSource(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "MANUAL", 1: "DAB", 2: "FM", 3: "SNTP" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.clock.source'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysClockTimeZone(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.clock.timeZone'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysClockUtcOffset(NodeS32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_S32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.clock.utcOffset'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysFactoryReset(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "NONE", 1: "RESET" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.factoryReset'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysInfoActiveSession(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "NO", 1: "YES" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.info.activeSession'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysInfoBuildVersion(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.info.buildVersion'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysInfoControllerName(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.info.controllerName'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysInfoDmruuid(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.info.dmruuid'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysInfoFriendlyName(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.info.friendlyName'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysInfoModelName(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.info.modelName'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysInfoNetRemoteVendorId(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.info.netRemoteVendorId'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysInfoRadioId(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.info.radioId'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysInfoRadioPin(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.info.radioPin'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysInfoRadiotest(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.info.radiotest'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysInfoSerialNumber(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.info.serialNumber'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysInfoVersion(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.info.version'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysIpodDockStatus(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "NOT_DOCKED", 1: "DOCKED_STILL_CONNECTING", 2: "DOCKED_ONLINE_READY", 3: "DOCKED_UNSUPPORTED_IPOD", 4: "DOCKED_UNKNOWN_DEVICE" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.ipod.dockStatus'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysIsuControl(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "IDLE", 1: "UPDATE_FIRMWARE", 2: "CHECK_FOR_UPDATE" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.isu.control'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysIsuMandatory(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "NO", 1: "YES" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.isu.mandatory'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysIsuSoftwareUpdateProgress(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.isu.softwareUpdateProgress'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysIsuState(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "IDLE", 1: "CHECK_IN_PROGRESS", 2: "UPDATE_AVAILABLE", 3: "UPDATE_NOT_AVAILABLE", 4: "CHECK_FAILED" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.isu.state'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysIsuSummary(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.isu.summary'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysIsuVersion(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.isu.version'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysLang(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.lang'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysMode(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.mode'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetCommitChanges(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "NO", 1: "YES" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.commitChanges'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetIpConfigAddress(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.ipConfig.address'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetIpConfigDhcp(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "NO", 1: "YES" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.ipConfig.dhcp'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetIpConfigDnsPrimary(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.ipConfig.dnsPrimary'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetIpConfigDnsSecondary(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.ipConfig.dnsSecondary'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetIpConfigGateway(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.ipConfig.gateway'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetIpConfigSubnetMask(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.ipConfig.subnetMask'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetKeepConnected(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "NO", 1: "YES" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.keepConnected'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetUapInterfaceEnable(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "INTERFACE_DISABLE", 1: "INTERFACE_ENABLE" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.uap.interfaceEnable'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetWiredInterfaceEnable(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "INTERFACE_DISABLE", 1: "INTERFACE_ENABLE" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.wired.interfaceEnable'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetWiredMacAddress(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.wired.macAddress'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetWlanActivateProfile(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.wlan.activateProfile'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetWlanConnectedSSID(NodeU):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.wlan.connectedSSID'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetWlanDeactivateProfile(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.wlan.deactivateProfile'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetWlanInterfaceEnable(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "INTERFACE_DISABLE", 1: "INTERFACE_ENABLE" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.wlan.interfaceEnable'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetWlanMacAddress(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.wlan.macAddress'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetWlanPerformFCC(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "TEST_STOP", 1: "TEST_START" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.wlan.performFCC'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetWlanPerformWPS(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "WPS_IDLE", 1: "WPS_PBC", 2: "WPS_PIN" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.wlan.performWPS'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetWlanProfiles(NodeList):
  def __init__(self) -> None:
    super().__init__()
    self.prototype = NodePrototype(args=[NodeArg('key', 1, 20), NodeArg('ssid', 32, 18)])

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.wlan.profiles'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetWlanRegion(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "INVALID", 1: "USA", 2: "CANADA", 3: "EUROPE", 4: "SPAIN", 5: "FRANCE", 6: "JAPAN", 7: "AUSTRALIA", 8: "Reserved8" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.wlan.region'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetWlanRegionFcc(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "NOT_ACTIVE", 1: "ACTIVE" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.wlan.regionFcc'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetWlanRemoveProfile(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.wlan.removeProfile'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetWlanRssi(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.wlan.rssi'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetWlanScan(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "IDLE", 1: "SCAN" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.wlan.scan'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetWlanScanList(NodeList):
  def __init__(self) -> None:
    super().__init__()
    self.prototype = NodePrototype(args=[NodeArg('key', 1, 20), NodeArg('ssid', 32, 18), NodeArg('privacy', 1, 17), NodeArg('wpsCapability', 1, 17), NodeArg('rssi', 1, 18)])

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.wlan.scanList'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetWlanSelectAP(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.wlan.selectAP'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetWlanSelectProfile(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.wlan.selectProfile'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetWlanSetAuthType(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "OPEN", 1: "PSK", 2: "WPA", 3: "WPA2" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.wlan.setAuthType'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetWlanSetEncType(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "NONE", 1: "WEP", 2: "TKIP", 3: "AES" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.wlan.setEncType'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetWlanSetFccTestChanNum(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.wlan.setFccTestChanNum'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetWlanSetFccTestDataRate(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "_1M", 1: "_2M", 2: "_5_5M", 3: "_11M", 4: "_22M", 5: "_6M", 6: "_9M", 7: "_12M", 8: "_18M", 9: "_24M", 10: "_36M", 11: "_48M", 12: "_54M", 13: "_72M" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.wlan.setFccTestDataRate'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetWlanSetFccTestTxDataPattern(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.wlan.setFccTestTxDataPattern'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetWlanSetFccTestTxPower(NodeU8):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.wlan.setFccTestTxPower'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetWlanSetFccTxOff(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "TX_ON", 1: "TX_OFF" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.wlan.setFccTxOff'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetWlanSetPassphrase(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.wlan.setPassphrase'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetWlanSetSSID(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.wlan.setSSID'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysNetWlanWpsPinRead(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.net.wlan.wpsPinRead'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysPower(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "OFF", 1: "ON" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return True
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.power'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysRsaPublicKey(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.rsa.publicKey'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysRsaStatus(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "GENERATION_IN_PROGRESS", 1: "KEY_AVAILABLE" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return True
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.rsa.status'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysSleep(NodeU32):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_U32))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.sleep'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseSysState(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "NORMAL_MODE", 1: "SAPU_MODE" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return True

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.sys.state'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseTestIperfCommandLine(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.test.iperf.commandLine'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseTestIperfConsole(NodeC):
  def __init__(self, value: str = None) -> None:
    super().__init__(value, 1024)
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_C))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.test.iperf.console'
  
  def get_prototype(self) -> str:
    return self.prototype

class BaseTestIperfExecute(NodeE8):
  def __init__(self, value: int = 0) -> None:
    super().__init__(value, { 0: "STOP", 1: "START" })
    self.prototype = NodePrototype(arg=NodeArg(data_type=ARG_TYPE_E8))

  @staticmethod
  def is_cacheable() -> bool:
    return False
  
  @staticmethod
  def is_notifying() -> bool:
    return False

  @staticmethod
  def is_readonly() -> bool:
    return False
  
  @staticmethod
  def get_name() -> str:
    return 'netRemote.test.iperf.execute'
  
  def get_prototype(self) -> str:
    return self.prototype
