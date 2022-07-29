# Compression-Algorithm used on the Core-System

![LastEdit](https://img.shields.io:/static/v1?label=LastEdit&message=07/26/2022&color=9cf)
![Status](https://img.shields.io:/static/v1?label=Status&message=TRASHED&color=darkred)
![Scripts](https://img.shields.io:/static/v1?label=Scripts&message=None&color=red)

This document of takes a more detailed look at the compression algorithm that is used to compress the main filesystem of Frontier Silicon devices in update files. For a detailed review of the FSAPI (NetRemoteApi) by Frontier-Silicon, take a look the following document: [`api-2.0`](api-2.0.md). 

It is recommended to take a look at the [`firmware-2.0`](firmware-2.0.md) document for a detailed review of the firmware binaries that are used to update Frontier Silicon devices.

## 1 Compression-Algorithm Theory
---
This chapter tries to discusses some popular compression algorithms and of course it tries to apply them on the compressed core system. At first, the binary data has to be extracted. 

The field `CompSize` defines the size of the first partition included in the firmware file. To to that, the `ISU Inspector Tool` can be used. It copies the compressed section into a file that is named like the input file plus a `core.bin` extension.

```bash
python3 isu_inspector.py -if FILE.isu.bin -e --core
# or execute the module directly
python3 -m fslib -if FILE.isu.bin -e --core
```
---
[compression signatures](https://github.com/frizb/FirmwareReverseEngineering)
