# FSAPI Implementation in Python3

![LastEdit](https://img.shields.io:/static/v1?label=LastEdit&message=07/24/2022&color=9cf)
![Status](https://img.shields.io:/static/v1?label=Status&message=DRAFT&color=orange)
![Dependencies](https://img.shields.io:/static/v1?label=Dependencies&message=urllib3&color=yellowgreen)

This document of takes a more detailed look at the implementation of the Frontier Silicon API (FSAPI) that is used to interact with Frontier Silicon devices. For a detailed review of the firmware binaries that are used to update Frontier Silicon devices, take a look the following document: [`firmware-2.0`](firmware-2.0.md).

This API Implementation includes all possible `Nodes` that can be interacted with. Additionally, the API comes with a module called `isudata` to use the backend service by the update-file provider. The most important information: Are there any dependencies? - **No**, besides `urllib3` which should be installed by default, everything can be used without downloading extra dependencies.

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#1-isudata">isudata</a>
      <ul>
        <li><a href="#11-class-definitions">Class Definitions</a></li>
        <li><a href="#12-function-defintions">Function Defintitions</a></li>
      </ul>
    </li>
    <li>
      <a href="#2-netremote">netremote</a>
      <ul>
        <li><a href="#11-class-definitions">Class Definitions</a></li>
        <li><a href="#12-function-defintions">Function Defintitions</a></li>
      </ul>
    </li>
    <li>
      <a href="#3-fsapitool">fsapi_tool</a>
      <ul>
        <li><a href="#31-isu-firmware-context">ISU Firmware Context</a></li>
        <li><a href="#32-node-exploration">Node Exploration</a></li>
        <li><a href="#33-interaction-with-the-device">Interaction with the device</a>
        <ul>
          <li><a href="#331-request-a-simple-property">Request a simple property</a></li>
          <li><a href="#332-query-property-lists">Query property lists</a></li>
          <li><a href="#333-apply-a--verbosealue-to-a-stored-property">Apply a value to a stored property</a></li>
        </ul>
      </ul>
    </li>
  </ol>
</details>

---
## 1. `isudata`

The backend used to find and download updates is located at `update.wifiradiofrontier.com`. To interact with the underlaying API, the `isudata`-module comes with two main-methods:

### 1.1 Class Definitions
---
```python
class ISUSoftwareElement:
  def __init__(self, 
    customisation: str = None, 
    version: str = None, 
    download_url: str = None, 
    mandatory: bool = False, 
    md5hash: str = None, 
    product: str = None, 
    size: int = 0, 
    vendor: str = 'Frontier Silicon', 
    summary: str = None
  ) -> None
```
The class contains all information needed to distinguish an update entry. Use the `loadxml` function to import data from a XML-Element. 

### 1.2 Function Defintions
---
```python
def isu_find_update(mac: str, customisation: str, version: str, verbose: bool = False, netconfig: fsapi.FSNetConfiguration = None) -> dict
```
* `mac` [`str`]: The MAC-Address string of a frontier silicon device in the following format: `002261xxxxxx`. This string must start with `002261`.
* `customisation` [`str`]: Information about the used interface, module and version number
* `version` [`str`]: As the name already states, the full version string. 
* `verbose` [`bool`]: if enabled/True, error messages will be printed to stdout
* `netconfig` [`FSNetConfiguration`]: if a custom configuration like a proxy should be used, this object can be passed as a parameter
* `@return` none if an error occurred or a dictionary with the following structure if an update is present:
  ```python
  return {
    'update_present': $update_is_present, 
    'headers': $response.headers, 
    'updates': [ $update_list ]
    }
  ```
* `@usage`:
  ```python
  # without custom netconfig -> HTTPS traffic
  response = fsapi.isu_find_update('$MAC', '$CUSTOM', '$VERSION')

  # with custom config -> force HTTP traffic
  config = fsapi.FSNetConfiguration(http_pool=urllib3.HTTPConnectionPool('$HOST'))
  response = fsapi.isu_find_update('$MAC', '$CUSTOM', '$VERSION', netconfig=config)

  ```
---
It is recommended to use the following function if the download-url is known or retrieved through the `isu_find_update` method.

```python
def isu_get_update(path: str, url: str = None, software: ISUSoftwareElement = None, verbose: bool = False, netconfig: fsapi.FSNetConfiguration = None) -> None:
```
* `path` [`str`]: an absolute or relative path to the output file
* `url` [`str` | `None`]: optional the direct download link - if not set, the software parameter must be defined
* `software` [`ISUSoftwareElement`]: the software object containing the relevant data for downloading the update file
* `verbose` [`bool`]: if enabled/True, error messages will be printed to stdout
* `netconfig` [`FSNetConfiguration`]: if a custom configuration like a proxy should be used, this object can be passed as a parameter
* `@return` nothing
* `@usage`:
  ```python
  # without custom netconfig -> HTTPS traffic
  response = fsapi.isu_find_update('$MAC', '$CUSTOM', '$VERSION')
  for _software in response['updates']:
    fsapi.isu_get_update('$FILE_PATH', software=_software)
  ```




<div style="text-align:right">
<a href="#fsapi-implementation-in-python3">Back to the top</a> | <a href="#1-isudata">1. isudata</a>
</div>

## 2. `netremote`

The next and last module of this small API implementation focusses on the `FsNetRemoteLib`. All nodes that are presented here were converted from the `Java`-source code of the app `Medion Lifestream 2`. The script, used for converting the code is placed in the directory `apk/`. The source code was converted because `nodes.py` contains more that 4000 lines of code in the end (to much work by hand).

When querying a resource or trying to set value to a specific node, there is always a status message that comes along with the response. The possible values for this status are:

| Status | Body | Description |
| --- | --- | --- |
| `FS_OK` | True | If everything goes right the status is set to `FS_OK` |
|`FS_PACKET_BAD`| False | This status code will be returned if a value should be applied to a read-only node. |
| `FS_NODE_BLOCKED` | False | Sometimes this status is given, maybe because the node was deactivated on the device. |
|`FS_NODE_DOES_NOT_EXIST` | False | As the name already states, the requested node is not implemented on that device. |
|`FS_TIMEOUT`| False | The device takes too long to respond| 
| `FS_FAIL` | False | If the parameters given in the url are mot matching the node criteria, the request will fail. |

### 2.1 Class Definitions
---
Because this module contains a lot of class definitions, only the most relevant are shown and described here.

```python
class NodeArg:
  def __init__(self, name: str, length: int, data_type: int) -> None

class NodePrototype:
  def __init__(self, arg: NodeArg, args: list[NodeArg]) -> None
```
The first two classes are used to add a prototype template to each node. By adding a `NodeArg` to a `NodePrototype` object, the same parameter has to be specified when calling the `netremote_request('SET', ...)` method. A small example should show the importance:

```python
# <in spcific Node class> -> do not change this code 
# Creating a prototype for the default parameter 'value' of type ui16.
prototype = NodePrototype(arg=NodeArg(data_Type=ARG_TYPE_U16))

# <custom code>
# If calling the SET method, the parameter has to be given
result = fsapi.netremote_request('SET', $node_class, $radio, parameters={'value': 1})
```
There are only a few `ARG_TYPE` values implemented and possible to use. These are: 

    ARG_TYPE_C:   int = 0x10  # C8-Array (char array) 
    ARG_TYPE_E8:  int = 0x11  # Type defined by an Enum
    ARG_TYPE_U8:  int = 0x12  # unsigned char
    ARG_TYPE_U16: int = 0x13  # unsigned short
    ARG_TYPE_U32: int = 0x14  # unsigned int
    ARG_TYPE_S8:  int = 0x15  # signed char
    ARG_TYPE_S16: int = 0x16  # signed short
    ARG_TYPE_S32: int = 0x17  # signed int
    ARG_TYPE_U:   int = 0x18  # array of data


The node classes represent the base of all possible functionalities this API provides. The package name of each node class can be fetched by calling the static method `node_class.get_name()`. Use `fsapi.get_all_node_names()` to get all implemented nodes.

Each node provides the following attributes: `cacheable` [`bool`], `notifying` [`bool`], `readonly` [`bool`], `<static>package_name` [`str`], `prototype` [`NodePrototype`] and the stored value in case the node is not a `NodeList`. These node list classes just contain a list of `NodeListItem`s, which can contain one ore more fields. These are packed into a dictionary named `attr`.

To make the import of `NodeList`s and `NodeListItem`s easier, these classes come with an inbuild function named `loadxml()`. Note that the XMLElement always needs to be the root element. For a more accurate review of the FSAPI, see the [fsapi](https://github.com/flammy/fsapi)-repository on Github. 

Before the functions, that are used to interact with the device are described, one last class has to be introduced:

```python
class RadioHttp:
  def __init__(self, host: str, pin: str) -> None
```
* `host` [`str`]: the ip-address or hostname of the device in the local network
* `pin` [`str`]: the used pin for that device (usually '`1234`')
* `@usage`:
  ```python
  radio = fsapi.RadioHttp('$IP')
  result = fsapi.netremote_request('GET', node_class, radio)
  ```

This class stores values that are used by the following functions:

### 2.2 Function Definitions
---
```python
def netremote_request(method: str, node_class, radio: RadioHttp, netconfig: FSNetConfiguration, parameters: dict[str, Any]) -> ApiResponse
```
* `method` [`str`]: the dedicated method to use (one of the following: `GET`, `SET`, `LIST_GET_NEXT`, `CREATE_SESSION`). `GET_MULTIPLE` and `SET_MUTLIPLE` is not supported yet.
* `node_class` [`class`]: the class type of the node which will be queried
* `radio` [`RadioHttp`]: the radio object storing the pin value and the target host string
* `netconfig` [`FSNetConfiguration`]: if a custom configuration like a proxy should be used, this object can be passed as a parameter
* `parameters` [`dict`]: used if a list of items is queried or a new value should be applied to a node. Please refer to the related node class, which parameters are accepted (if there is no argument name, use `value` as parameter name).
* `@return` an ApiReponse object including a node instance with the gathered value
* `@usage`:
```python
# SET request
result = fsapi.netremote_request('SET', fsapi.nodes.BaseSysInfoFriendlyName, $radio, parameters={'value': "Hello World"})

# GET request
result = fsapi.netremote_request('GET', fsapi.nodes.BaseSysInfoFriendlyName, $radio)

# LIST_GET_NEXT request
result = fsapi.netremote_request('LIST_GET_NEXT', $node_class, $radio, parameters={'maxItems': 100})
```
---
In order to get all node names (package names) or all implemented node classes, the following utility methods can be used:
```python
def get_all_node_names() -> list[str]
def get_all_node_types() -> dict[str, type]
```

<div style="text-align:right">
<a href="#fsapi-implementation-in-python3">Back to the top</a> | <a href="#2-netremote">2. netremote</a>
</div>

## 3 fsapi_tool
---

To bundle all features this API contains, a small tool names `fsapi_tool.py` was created. Allthough, there is a file which can be executed, the module `fsapi` also has a `__main__.py` file in order to directly execute the module with `python3 -m fsapi`. Because the API consits of different actions that can be made, there are different contexts in this tool.

> **Important:** this command line tool does not provide any custom HTTP or proxy configuration. Requests to devices must be done with HTTP and to the web-backend by default HTTPS is used.

The basic structure of each command can be stated as follows:

```console
$ python3 -m fsapi $context [context_args] $Host_Address [-W/--pin PIN] [--verbose/---verboseerbose]
```
Each command must specify the host address in order to define the target machine. Additionally, if the pin was changed, it can be added via `-W/--pin`. Note that there will be output on the console only if `--verbose/---verboseerbose` was given.

### 3.1 ISU Firmware Context
---
The first context is named `isu`. Here, the download link for the firmware can be searched or generated and optional the file can be downloaded directly.

#### `@usage`

```console
usage: __main__.py isu [-h] [--find] [--collect PATH] [-F]

optional arguments:
  -h, --help      show this help message and exit
  --find          Find an update for the specified host. If none was found a download 
                  URL for the current version will be generated.
  --collect PATH  Collect the firmware to the specified path. (only together with 
                  --find)
  -F, --file      Collect the firmware from the specified path. (The ip-address parameter
                  will be treated as the filename)
```

#### `@example`
```bash
# Find update and display it or generate update url
python3 -m fsapi isu --find $IP_ADDRESS --verbose

# Find update and download to the file with $FILE_NAME
python3 -m fsapi isu --find --collect $FILE_NAME $IP_ADDRESS --verbose

# Download binaries from file
python3 -m fsapi isu --file ./bin/updates.txt
```

<div style="text-align:right">
<a href="#fsapi-implementation-in-python3">Back to the top</a> | <a href="#3-fsapitool">3. fsapi_tool</a>
</div>

### 3.2 Node Exploration
---
In order to enumerate all available nodes a user can interact with, there is a context named `explore`. The responses from every request can be saved using `--json`.

#### `@usage`
```console
usage: __main__.py explore [-h] [--json] [-E EXCLUDE]

options:
  -h, --help                     show this help message and exit
  --json                         Saves information in JSON-format in the
                                 current directory.
  -E EXCLUDE, --exclude EXCLUDE  Exclude the following arguments from 
                                 being analysed (if more that one, 
                                 separate them with a comma)
```

#### `@example`
```bash
# Display all responses (even failed ones)
python3 -m fsapi explore $IP_ADDRESS --verbose

# Display all responses without ones that have status_code == FS_NODE_DOES_NOT_EXISTS
python3 -m fsapi explore -E "FS_NODE_DOES_NOT_EXISTS" $IP_ADDRESS --verbose

# Display all responses without ones that have status_code == FS_NODE_DOES_NOT_EXISTS and save them in JSON-format 
python3 -m fsapi explore --json -E "FS_NODE_DOES_NOT_EXISTS" $IP_ADDRESS --verbose
```

<div style="text-align:right">
<a href="#fsapi-implementation-in-python3">Back to the top</a> | <a href="#3-fsapitool">3. fsapi_tool</a>
</div>

### 3.3 Interaction with the device
---
The next three contexts are written to interact with the device. Two of them are used to query properties and the last one to set properties to nodes. These commands do not work with the `--verbose/-v` flag and will always print their results. 

### 3.3.1 Request a simple property

To request a simple property the context `get` should be used.

#### `@usage`
```console
usage: __main__.py get [-h] -n NODE

options:
  -h, --help            show this help message and exit
  -n NODE, --node NODE  The netRemote package name. (format: 
                        netremote.xxx.xxx.xxx)
```

#### `@example`
```bash
# Fetch the display name of a device
python3 -m fsapi get -n netRemote.sys.info.friendlyName $IP_ADDRESS
```

<div style="text-align:right">
<a href="#fsapi-implementation-in-python3">Back to the top</a> | <a href="#3-fsapitool">3. fsapi_tool</a>
</div>

### 3.3.2 Query property lists

To request a property list the context `list` should be used.

#### `@usage`
```console
usage: __main__.py list [-h] -n NODE [--args [ARGS ...]]

options:
  -h, --help            show this help message and exit
  -n NODE, --node NODE  The netremote package name. (format: 
                        netRemote.xxx.xxx.xxx)
  --args [ARGS ...]     The arguments passed to the request. 
                        (format: --args arg:value [arg:value [...]]))
```

#### `@example`
```bash
# Query all valid modes of a device
python3 -m fsapi list -n netRemote.sys.caps.validModes --args maxItems:100 $IP_ADDRESS 
```

<div style="text-align:right">
<a href="#fsapi-implementation-in-python3">Back to the top</a> | <a href="#3-fsapitool">3. fsapi_tool</a>
</div>

### 3.3.3 Apply a value to a stored property

In order to control the device properties, the `set` context can be used. The command structure is similar to the `list` context.

#### `@usage`
```console
usage: __main__.py set [-h] -n NODE [--args [ARGS ...]]

options:
  -h, --help            show this help message and exit
  -n NODE, --node NODE  The netremote package name. (format: 
                        netRemote.xxx.xxx.xxx)
  --args [ARGS ...]     The arguments passed to the request. 
                        (format: --args arg:value [arg:value [...]]))
```

#### `@example`
```bash
# Set the display name
python3 -m fsapi set -n netRemote.sys.info.friendlyName --args value:"Hello World" $IP_ADDRESS
```

<div style="text-align:right">
<a href="#fsapi-implementation-in-python3">Back to the top</a> | <a href="#3-fsapitool">3. fsapi_tool</a>
</div>