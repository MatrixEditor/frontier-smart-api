<div align="center">

![logo](docs/graphics/company_logo.png)
</div>

# Frontier Smart API and Firmware Analysis

![LastEdit](https://img.shields.io:/static/v1?label=LastEdit&message=07/29/2022&color=9cf)
![Status](https://img.shields.io:/static/v1?label=Status&message=LAST-STAGE&color=grey)
![Platform](https://img.shields.io:/static/v1?label=Platforms&message=Linux|Windows&color=yellowgreen)

This repository contains different tools written in `python3` to examine properties of firmware binaries provided by Frontier Silicon (former Frontier Smart - FS) and to interact with the inbuild API. 

Allthough there are some repositories that focus on that specific API, the implementation provided here contains all available `Nodes` that were invented/developed by Frontier Smart. The nodes were converted from `java` source code (The [Tool](apk/node_converter.py) is also in this repository).

In order to use the tools provided by this repository, almost all available firmware binaries are located in the folder [`bin/`](bin/). Most of them were forked from [here](https://github.com/cweiske/frontier-silicon-firmwares).

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#documents">Documents</a></li>
    <li>
      <a href="#overview">Overview</a>
      <ul>
        <li><a href="#proxy-setup-with-zap">Proxy Setup with ZAP</a></li>
        <li><a href="#proxy-setup-with-burp-suite-commercial">Proxy Setup with Burp</a></li>
      </ul>
    </li>
    <li>
      <a href="#tools">Tools</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

---
## Documents

A detailed review of the firmware binaries that are used to update Frontier Silicon devicesis provided in the following document: [`firmware-2.0`](firmware-2.0.md). The FSAPI (NetRemoteApi) by Frontier-Silicon is described here: [`api-2.0`](api-2.0.md) and to view the research on gathering the compression algorithm used to compress the main filesystem, take a look at the [`compression-2.0`](compresion-2.0.md) document (*`under preparation`*).

## Overview
---

As stated above, this repository provides a uitlity to interact with the FSAPI (Frontier Smart API) and a research on how the firmware binaries are structured. Devices and Apps used within the research:

> `Medion MD87805`, Apps: `Lifestream II` and `UNDOK`

The source code for these apps were retrieved directly from a mobile device with the `adb`-tool:

```bash
# list all installed packages and search for the app
$ adb pm list packages
# get the path to the specified app
$ adb pm path ${app.package.com}
# pull the source code to the local machine
$ adb pull $PATH_TO_APK_FILE $LOCAL_PATH
```

In order to view the decompiled `java`-code, the `jadx`
-decompiler and `jadx-gui` were used. This tool also provides an export function to save the decompiled `java` sources locally.

The source code contains a package called `src/com/frontier_silicon/NetRemoteLib/Node/` where all available nodes are stored/ implemented with a `java` class each. There was also a [tool](apk/node_converter.py) created to convert these classes into python classes. To use  the generated code you have to copy [this](fsapi/netremote/basenode.py) python file.

Lets take a look at the network traffic produced by the internet radio. In order to capture all packets, a proxy could be very useful. Because there is no possibility to setup a simple proxy on that device, the traffic was captured directly on the connected wifi access point.

Anyway, if you want to intercept traffic of the mobile device where an app is running, the following steps are required:

<details>
<summary>Setting up a simple proxy</summary>

#### __Proxy Setup with ZAP__

1. ZAP: Goto Options > Dynamic SSL Certificate > Generate and save the file to the local storage
2. Copy the `cert`-file to the internal storage of the device
3. Android: Goto Settings > Search > Type `Certificate` > CA Certificate > Install Anyway and choose the file from the internal storage
4. ZAP: Goto Options > Local Proxies and remove the address of the proxy server > Ok
5. Android: Goto Settings > wifi > select the current wifi > Change Proxy to manual and enter host address of the proxy server together with the port.
6. Start the app

#### __Proxy Setup with Burp Suite (Commercial)__

1. Burp: Goto Proxy > Options > Add Proxy Listener, select bind to all Interfaces and provide a custom port
2. Android: visit http://burpsuite to download CA-Certificate > installation same with the ZAP proxy
3. Start the app
</details>

---
A quick look at the produced network traffic in wireshark reveals some interesting facts:

    * The communication between the device and clients is handled 
      with HTTP
    * Specific URLs are queried when looking for a software update. 
      These are:
        > update.wifiradiofrontier.com/FindUpdate.aspx
        > update.wifiradiofrontier.com/Update.aspx

The first URL returns `404` or `403` if no update is available. Is an update available, there will be a XML-response by the first URL-query. The structure is mentioned at the class defintion of [`ISUSoftwareElement`](docs/api-2.0.md#11-class-definitions).

The firmware binaries are located at the second URL with the mandatory parameter `f=/updates/xxx`. The name of the file is structured as follows:

```bash
> ir-$MODULE-$INTERFACE-$IFACEVERSION-${MODEL}_V$VERSION.$REVISION-$BRANCH
# on the internet radio device used here this expands to
> ir-mmi-FS2026-0500-0549_V2.12.25c.EX72088-1A12
```

Note that the file name in the URL replaces the `_V` with a simple dot. To download an update file, you can use the `fsapi_tool` or execute the `fsapi` module directly. The following command collects all firmware binaries specified in the given file.

```bash
$ python3 -m fsapi isu --file ./bin/updates.txt --verbose
# alternative with local device:
$ python3 -m fsapi isu --find --collect myFile $IP_ADDRESS --verbose
```
<p align="right">(<a href="#top">back to top</a>)</p>

## Tools

There are two tools included in this repository together with two python modules: `isu_inspector` and `fisu`, `fsapi_tool` and `fsapi`. Installation instructions follow:

<details>
  <summary>Installation</summary>

  #### __Prerequisites__

  Make sure you have installed the latest version of python `setuptools` and `pip`:
  ```bash
  $ pip install setuptools
  ```

  #### __Installation__

  This respository uses setuptools to install the python packages locally. All dependnecies used by the provided libraries should be installed by default. To install the preferred package, copy the `setup-XXX.py` file from the `setup/` directory and rename the file to `setup.py`:

  ```bash
  $ pip install .
  ``` 

  This command should install the selected library to the local site-packages. Now, you are good to go - execute the module with

  ```bash
  python3 -m $module --help
  ```

</details>

<details>
<summary>Example of <code>isu_inspector.py</code>:</summary>

    $ python3 -m fisu -if=./bin/FS2026/0500/ir-mmi-FS2026-0500-0015.2.5.15.EX44478-1B9.isu.bin --verbose --header

                    ISU-Inspector Tool
    ---------------------------------------------------------------------

    [+] Analyzing ISU File header...
      - MeOS Version: 1
      - Version: '2.5.15.EX44478-1B9'
        | SDK Version: IR2.5.15 SDK
        | Revision: 44478
        | Branch: 1B9

      - Customisation: 'ir-mmi-FS2026-0500-0015'
        | DeviceType: internet radio
        | Interface: multi media interface
        | Module: Venice 6 (version=0500)

    [+] SystemEntries:
      - SysEntry: type=FS, partition=1
      - SysEntry: type=FS, partition=2 (Could be DirectoryArchive for Web-Data)
      - SysEntry: type=END, magicnumber=0x81c9

    [+] Declared Fields:
      - DecompBuffer: Buffer=2957053952
      - CompSize: Size=1384319
      - DecompSize: Size=2621504
      - CodeSize: Size=7760
      - CompBuffer: Buffer=2952790016

</details>

<details>
<summary>Example of <code>fsapi_tool.py</code>:</summary>

    $ python3 -m fsapi set -n netRemote.sys.info.friendlyName --args value:MedionIR $IP_ADDRESS
    [+] fsapiResponse of netRemote.sys.info.friendlyName:
        - status: FS_OK

    $ python3 -m fsapi get -n netRemote.sys.info.friendlyName $IP_ADDRESS
    [+] fsapiResponse of netRemote.sys.info.friendlyName:
        - status: FS_OK
        - value: MedionIR
        - readonly: False
        - notifying: True

    $ python3 -m fsapi isu --find $IP_ADDRESS

    [+] Generating current URL...
        - url: https://update.wifiradiofrontier.com/Update.aspx?f=/updates/ir-mmi-FS2026-0500-0549.2.12.25c.EX72088-1A12.isu.bin
        
</details>

---
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
---
## License

Distributed under the MIT License. See `MIT.txt` for more information.

