# In-Depth Analysis of firmware binaries from Frontier Silicon

![LastEdit](https://img.shields.io:/static/v1?label=LastEdit&message=07/23/2022&color=9cf)
![Status](https://img.shields.io:/static/v1?label=Status&message=DRAFT&color=orange)
![Dependencies](https://img.shields.io:/static/v1?label=Dependencies&message=None&color=green)

This document of takes a more detailed look at the firmware binaries that are used to update Frontier Silicon devices. For a detailed review of the FSAPI (NetRemoteApi) by Frontier-Silicon, take a look the following document: [`api-2.0`](api-2.0.md). To view the research on gathering the compression algorithm used to compress the main filesystem, take a look at the [`compression-2.0`](compresion-2.0.md) document.

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#1-binary-analysis">Binary analysis</a>
      <ul>
        <li><a href="#11-header-structure">Header structure</a></li>
        <li><a href="#12-system-entries">System Entries</a></li>
        <li><a href="#13-compressiondecompression-buffers">Compression/Decompression Buffers</a></li>
        <li><a href="#14-isu-file-structure">ISU File structure</a></li>
      </ul>
    </li>
    <li>
      <a href="#2-directory-archive">Directory Archive</a>
      <ul>
        <li><a href="#21-contents-of-a-directory-archive">Contents of a Directory Archive</a></li>
      </ul>
    </li>
    <li>
        <a href="#3-isu-inspector">ISU-Inspector Tool and API</a>
        <ul>
            <li><a href="#31-isuisuwalk">isu.isuwalk</a></li>
            <li><a href="#32-isufsversion">isu.fsversion</a></li>
        </ul>
    </li>
    <li>
      <a href="#4-compressed-code">Compressed Code Analysis</a>
    </li>
  </ol>
</details>

---
Due to the fact that Frontier Silicon devices as well as the inspected MEDION device uses a custom OS, it makes the undestanding of the firmware files more difficult. As [this](https://web.archive.org/web/20180210192501/https://certifications.prod.wi-fi.org/pdf/certificate/public/download?cid=WFA55569) Wifi-ceritficate states, the `Venice 6.5` module by Frontier-Silicon is using the **`MeOS`** with version 5.2 ([source](https://github.com/MIPS/meos/blob/master/doc/rst/manual.rst)). A brief description follows:

> The MEOS (MIPS Embedded Operating System) provides a framework that allows systems programmers to design systems as loosely coupled collections of tasks and device driver modules, with the details of scheduling, synchronisation and communication being handled by a standardised and well tested environment.

This brings us back to the begiginning, because this embedded OS is just a framewark which can be used to develop the operating system. 

## 1. Binary Analysis
---
There are several ways to determine the filetype. in this case the following tools are used: `file`, `binwalk`, `dd`, `vbindiff` and to view the binary data in a hex-editor: `bless`.

Starting off with the `file` utility:
~~~console
$ file ir-mmi-FS2026.isu.bin 
ir-mmi-FS2026.isu.bin: data
~~~

Just gives `data` as result. Now, lets take a look on the same file with `binwalk`:
~~~console
$ binwalk -B -A -t ir-mmi-FS2026.isu.bin

DECIMAL       HEXADECIMAL     DESCRIPTION
------------------------------------------------------------------------------------
1399391       0x155A5F        AES Inverse S-Box
1400762       0x155FBA        SHA256 hash constants, little endian
2032581       0x1F03C5        SHA256 hash constants, little endian
2039377       0x1F1E51        AES Inverse S-Box
2622703       0x2804EF        Zlib compressed data, best compression
2635012       0x283504        PNG image, 120 x 120, 8-bit/color RGBA, non-interlaced
2635097       0x283559        Zlib compressed data, best compression
2637769       0x283FC9        Zlib compressed data, best compression
[...]
~~~

Now there is a much more detailed result on what contents are stored in the firmware file. Note that the offset - the beginning of the compressed data - starts at `0x2804EF` (~ 2.6Mb). This is an important information, because the data section before that offset is not used in the `binwalk` analysis.

To view the contents stored in the directory archive the tool `isu_inspector.py` is used (stored in this repository). Type the follwing command in order to retrieve an accurate view of the stored data:

~~~console
$ python3 isu_inspector.py -if FILE.isu.bin -of archive.xml --archive --verbose
~~~
A small description on the used parameters:
    
    if (Input File): the input binary
    of (Output File): a path to the output file of type .xml
    archive (Directory Archive): inspects the directory archive stored in the binary
    verbose: print extracted information 

A file entry in the output saved to `archive.xml` could be like this:
~~~xml
[...]
<file type=0, name="index.html", size=1876, offset=109867, compressed="True", compression_size=762, real_offset=2731787 />
[...]
~~~

With the command line utility `dd` the file can be copied. Here, the `index.html` file is extracted:
~~~bash
$ dd if=FILE.isu.bin of=index.html bs=1 offset=2731787 count=762
~~~
The `real_offset` value is used - it represents the offset in relation to the start of the binary. Because the file is compressed, the right compression tool should decompress it. Alternatively, `binwalk` can extract the contents at runtime. Unfortunately, these results are named by their offset position, e.g. the `2804EF` file stores image-data. To solve this problem, use the `ISU-Inspector Tool` with the `-e` flag to automatically extract (not decompress) archive files.

The files stored in the directory archive are exposed via a web interface to the user (if a web interface is present). They can be accessed by typing in the following url: `http://<IP>/<Path to File>.<Extension>`

### 1.1 Header structure
---

There is a specific file header for the update files which contains additional information about the firmware file. The basic structure can be defined as follows: **All numbers are little endian**

    ┌───────────────────────────────────────────────────────────────────┐
    │ ISU.BIN File Header                                               │
    ├────────────────────┬──────────────────────┬───────────────────────┤
    │ signature: uint_32 │ header size: uint_32 │ meos version: byte[4] │
    ├───────────────────┬┴──────────────────────┴─┬─────────────────────┤
    │ version: byte[32] │ customisation: byte[64] |   rdata: byte[16]   |
    └───────────────────┴─────────────────────────┴─────────────────────┘

* `Signature`: A sequence of bytes: `76 11 00 00` representing the file signature
* `Header Size`: A uint_32 (4 bytes) big number specifying the length of this header. This value is always `0x7c = 124`.
* `MeOS Version`: The next four bytes may be used to indicate the `MeOS MajorVersion` and `MeOS MinorVersion`.
* `Version`: The next 32 bytes are reserved for the version string. If the actual content does not reach 32 characters, all other are filled up with `0x20` = a whitespace.
* `Customisation`: The next 64 bytes are reserved for the firmware string. If the actual content does not reach 64 characters, all other are filled up with `0x20` = a whitespace.

### 1.2 System-Entries
---
Subsequently, there is some data which will be described below. Note, that this data section starts immediately after the header size offset at `0x7C`. This data will be named `System-Entry-Table` as these entries always have a size of 16 bytes and maybe indicate what partitions this file contains.

    ┌──────────────────────────────────────────────────────────┐
    │ ISU-System Entry                                         │
    ├────────────────────┬───────────────────┬─────────────────┤
    │ indicator: uint_32 │ fs_number: uint_4 │ fs_type: uint_4 │
    ├──────────────────┬─┴───────────────────┴──┬──────────────┤
    │ pattern: byte[7] │ entry pattern: byte[4] │              │
    └──────────────────┴────────────────────────┴──────────────┘

Where
* `Indicator`: is represented by `50 00 10 00` sequence,
* `FS_Number`:  usually a running number starting from `0x01`. If the number in the next entry does not follow the previous one it should be the last entry.
* `FS_Type`: `A8` to indicate a partition and `B8` for the last entry.
* `Pattern`: the next bytes are generated as follows: `0A 00 00 Bx 0A 00`, where `x` is again a running number starting from 4 and steps with 4 
* `EntryPattern`: A pattern that is unique for each entry category. The pattern for the last entry could be an identifier for the SDK Version this firware file was built. 

The structure (hex-format) of what these values could apply to:

> <span style="color:darkgrey">50 00 10 00 </span><span style="color:lightgreen">xx xx</span> <span style="color:darkgrey">0A 00 B</span><span style="color:lightgreen">x xx</span> <span style="color:darkgrey">0A 00</span> <span style="color:lightgreen">xx xx xx xx</span>  

It appears that the first byte after the indicator are used to identify the partition. From what the inspected files have shown, the values accept the following structure:

    : 10 A8 > the first partition containing the software
    : 20 A8 > the second partition containing web-data

The next suggestion is whether only the first 4 bits are taken and compared to the following (this pseudocode tries to describe the process of how to evaluate the entry):

    value  := uint_8(buffer)
    number := (value & 0xF0) >> 4 
    # (0b00010000 & 0b11110000) >> 4 = 0b00000001

    if number is prev_number + 1 then 
      entry := entry(number)
    else 
      entry := last entry
      
The first and second entry are equal compared to other firmware files that use the same `Venice 6` module. Obiously, the 1st and 9th byte of the last entry subtracted gives us `0x02`. Therefore, this may be a check to verify this entry:

    if entry_1st_byte - 2 is not entry_9th_byte:
      throw error: 'malformed entry'


### 1.2.1 Unidentified Section 1
---
Right after the two or three system entries, there is a block of data until offset postition `0x28c` (`652`) and is filled with `0x00`. This section, starting immediantly at the offset, consists of two `uint_16` values in the beginning that are equal among the checked firware binaries. The structure can be describes as follows:

    ┌──────────────────────────────────────────┐
    │ Section I                                │
    ├────────────────────┬─────────────────────┤
    │ Indicator: uint_16 │ block size: uint_16 │
    ├────────────────────┼─────────────────────┤
    │ filler data: bytes │ end value: uint_16  │
    └────────────────────┴─────────────────────┘

In this section (and the followiong ones), the indicator applies to `0x0580`. Directly after that, the block size is specified with a `uint_16`. Until the end of the block there is some filler data, which is filled with the following algorithm:

$$
fillerCount := {BlockSize \over 12}, 
$$

when `12` is the size of each filler data block. At the end, there is another `uint_16` value. Yet, the meaning of this value is unidentified. Until the next section, starting with the same indicator as this section, the data is filled up with `0x00`.

### 1.2.2 Unidentified Section 2
---
Starting off with the same indicator as defined before in the previous chapter, this data section is a bit more different compared to the previous one. Allthough, the overall structure is the same, the meaning might me different.

    ┌──────────────────────────────────────────────────────────────────────────────────────┐
    │ Section II                                                                           │
    ├────────────────────┬─────────────────────┬───────────────────────────┬───────────────┤
    │ Indicator: uint_16 │ block size: uint_16 | data_block: byte[12 | 8]  │ tail: uint_16 │
    └────────────────────┴─────────────────────┴───────────────────────────┴───────────────┘

The blocks of data are split up into arrays of bytes with a length of 8 or 12. Because there has been no system behind these data blocks found yet, the structure of these blocks will not be described. As above, there is a tail of two bytes. 

### 1.2.3 Unidentified Section 3
---
It is notable, that this data section starts with the same identifier as the both sections above. So, the structure is the following:

    ┌────────────────────────────────────────────┐
    │ Section III                                │
    ├────────────────────┬─────────────────────┬─┤
    │ Indicator: uint_16 │ block size: uint_16 │ │
    ├────────────────────┴──┬──────────────────┴─┤
    │ filler data: byte[12] │ end value: uint_16 │
    └───────────────────────┴────────────────────┘

Until the next section, starting with the same indicator as this section, the data is filled up with `0x00`.

### 1.2.4 Unidentified Section 4
---
The last section before some raw data, where the compression and decompression buffer follows, contains just 246 bytes. 

    ┌────────────────────────────────────────────┐
    │ Section IV                                 │
    ├────────────────────┬─────────────────────┬─┤
    │ Indicator: uint_16 │ block size: uint_16 │ │
    ├────────────────────┴──┬──────────────────┴─┤
    │ filler data: byte[12] │ end value: uint_16 │
    └───────────────────────┴────────────────────┘

Because there are three (four) sections, that almost have the same structure there will be a detailed description of the individual data blocks in the future as there is some kind of structure in them.

### 1.2.5 Unidentified Section 5
---
As described above, the four section is following some raw data, which can also be structured:

    ┌───────────────────────────────────────────┐
    │ Section V                                 │
    ├────────────────────┬──────────────────────┤
    │ Indicator: uint_16 │ block_count: uint_16 │
    ├──────────────────┬─┴──────────────────────┤
    │ Unknown: uint_16 │ data_blocks: bytes[12] │
    └──────────────────┴────────────────────────┘



### 1.3 Compression/Decompression Buffers 

The next section starts at offset `2768`. The data between this offset and the last entry may be just a filler. A the name of this chapter states, that the following data could be used to identify the compressed file size (it is so). The structure is given below:

    ┌──────────────────────────────────────────────────────────┐
    │ ISU-Decomp/Comp/Code -Size or Buffer                     │
    ├────────────────────┬──────────────────┬──────────────────┤
    │ indicator: uint_32 │ name_len: uint_8 │ pattern: byte[3] │
    ├───────────┬────────┴────────────┬─────┴─────────┬────────┤ ▲
    │ name: str │ filler block: bytes │ size: uint_32 │        │ │
    ├───────────┴─────────────────────┴───────────────┘        │ │ byte[24]
    │                   filler bytes: byte[4]                  │ │
    └──────────────────────────────────────────────────────────┘ ▼

* `Indicator`: Starting off with `20 00 00 53` as the indicator
* `NameLen`: The next byte specifies the length of the fields' name.
* `Pattern`: Before the name string a small pattern that consits of `00 04 00` has to be defined.
* `Name`: as the name of this part already states, it contains the field name
* `FillerBlock`: As the size of the field is limited to 24 bytes this block is designed to fill up the first bytes with `00` until there are only 8 bytes left.
* `Size` (or `Buffer`): the first 4 bytes of the last 8 could specify the size or buffer linked to the given field.

Note, that the value provided byte the `CompSize`-Field specifies the compressed size of the first partition. 

### 1.4 ISU-File structure
To conclude what this chapter revealed about the file structure a small graphic will be presented below:

    ┌─────────────────────────────────────────────────┐
    │ ISU Firmware Binary                             │
    ├───────────────────────┬─────────────────────────┤
    │ FileHeader: byte[124] │ SystemEntryTable: bytes │
    ├───────────────────────┴─────────────────────────┤
    │                                                 │
    │                 rdata: bytes                    │
    │                                                 │
    ├─────────────────────────┬───────────────────────┤
    │ FieldEntries: byte[195] │                       │
    ├─────────────────────────┘                       │
    │                                                 │
    │                 rdata: bytes                    │
    │                                                 │
    ├─────────────────────────────────────────────────┤
    │                                                 │
    .                                                 .
    .      CompressedDataBlock: sizeof(CompSize)      .
    .                                                 .
    │                                                 │
    ├───────────────────┬─────────────────────────┬───┤ ▲
    │ rdata: byte[5308] │ DirectoryArchive: bytes │   │ │
    ├───────────────────┴─────────────────────────┘   │ │
    │                                                 │ │ optional
    │           CompressedFileData: bytes             │ │
    │                                                 │ │
    └─────────────────────────────────────────────────┘ ▼

* `FileHeader`: Together with the file signature and some useful data, this section could be used to verify the firmware binary by the device.  (see [1.1 Header Strucure](#11-header-structure))
* `SystemEntryTable`: The next data section provides the stored partition information. (see [1.2 System-Entries](#12-system-entries))
* `rdata`: some filler blocks
* `FieldEntries`: As the size of each field definition is fixed to be 39 bytes. The whole section (including 5 fields) takes 195 bytes of this file. (see [1.3 Compression/Decompression Buffers](#13-compressiondecompression-buffers))
* `CompressedDataBlock`: This data section might be the most interesting, because it contains the compressed source of the firmware.
* `DirectoryArchve`: An optional section of data that specifies the stored web-data.
* `CompressedFileData`: Allthough, not all data included in this section is compressed, it will be named like it does have only compressed data. (see [2.0 Directory Archive](#2-directory-archive))

## 2. Directory Archive
---
Directory Archives are by far the most common structure in use today. As the name suggests, these archives store a directory that lists details about all the files, such as their name, offset and length. These archives are usually simple and very easy to read.

The structure of the `Directory Archive` used in the firmware binaries is following one:

> The Directory archive starts with a header tag called `FSH1`.  Directly after that, the size of the archive and the size of the index is presented as 32bit numbers. The actual structure of each entry in the archive index is the following: | type: uint_8 | entry_specific: bytes |

The type is defined as `0x00` = directory and `0x01` = file.

    ┌──────────────────────────────────────────┐
    │Archive Header                            │    
    ├───┬──────────────────────────────────────┤    
    │   │ - header tag:     str      = FSH1    │    
    │   │ - size:           uint_32            │    
    │   │ - magic_number:   uint_16            │    
    │   │ - index size:     uint_32            │    
    ├───┴──────────────────────────────────────┤       
    │                                          │    
    ├──────────────────────────────────────────┤    
    │Directory                                 │
    ├───┬──────────────────────────────────────┤
    │   │ - name length:    uint_8             │
    │   │ - name:           str                │
    │   │ - entries:        uint_8             │
    ├───┼──────────────────────────────────────┤
    │   │File Entry 1                          │
    ├───┼───┬──────────────────────────────────┤
    │   │   │ - name length:      uint_8       │
    │   │   │ - name:             str          │
    │   │   │ - file size:        uint_32      │
    │   │   │ - file offset:      uint_32      │
    │   │   │ - file compression: uint_32      │
    ├───┴───┴──────────────────────────────────┤
    │...                                       │
    ├──────────────────────────────────────────┤
    │File Data                                 │
    ├───┬──────────────────────────────────────┤
    │   │File Data 1                           │
    │   ├───┬──────────────────────────────────┤
    │   │   │ - file data:       bytes         │
    └───┴───┴──────────────────────────────────┘

To view the contents stored in the directory archive the tool isu_inspector.py is used (stored in this repository). Type the follwing command in order to retrieve an accurate view of the stored data. Additionally, you can use `-e` to extract the files afterwards. Note that these files might be compressed and their file names might let you assume they are not.

    $ python3 isu_inspector.py -if FILE.isu.bin [-e] --archive --verbose

### 2.1 Contents of a Directory Archive

The structure a defined directory archive in ISU-Files differs not that much. The tree structure can be represented as follows:

    icons/
    web/
        css/
        images/
        iperf/ (optional)
        js/
        languages/
        <HTML-Files>
    FwImage/

The structure alone reveals some interesting information that was still unknown. The `iperf` directory contains files that are built to interact with an inbound `iperf` module. 

> iPerf3 is a tool for active measurements of the maximum achievable bandwidth on IP networks. ([link](https://iperf.fr/))

Looking at `FwImage`, the directory might contain a firmware image, which is absolutely right. Usually the file stored here is the latest firmware image for the inbuild Wifi-Chip.

## 3. ISU-Inspector
---
This chapter contains a brief instruction overview to the internal tool and API provided by this repository. Named `fisu`, the API can be used to parse a directory archive, system-table-entries and field declarations with `isuwalk`. Additionally, the internal storage object model is realized by a custom XML-Tree structure named `FshTree` and `FshElement`. 

In order to describe the version and customisation of a firmware binary the classes `FSCustomisation` and `FSVersion` in `fsversion` are used.

Help page
```console
$ python3 isu_inspector.py --help
# or 
$ python3 -m fisu --help
usage: isu_inspector.py [-h] -if IF [-of OF] [--verbose] [--header] [--archive] [--sig SIG] [-e] [--core]

options:
  -h, --help     show this help message and exit
  -if IF         The input file (must have the *.isu.* extension)
  -of OF         The output file (Format: XML).
  --verbose      Prints useful information during the specified process.

information gathering:
  --header       Parses the header of the given file and extracts information.
  --archive      Parses the virtual filesystem.
  --sig SIG      The path to the 'file_sigs.json file'. This option includes the signature search.

extract data:
  -e, --extract  Extract data (usually combined with other parameters).
  --core         Extract the compressed core partition source.
```

### 3.1 **isu.isuwalk**

A small module written for fast analysis and parsing of ISU-firmware files. It contains different methods and constants.

---
To parse the directory archive index, use `isu_parse_entry`. The function will delegate the execution to `_parse_file` or `_parse_dir`.

    isu_parse_entry(root: FshElement, index, start, offset, buffer, level=0, verbose=False) -> tuple[int, int]

* `root` [`FshElement` | `None`]: if the entries in the index of the directory archive should be stored into an object, this parameter should not be `None`. 
* `index` [`int`]: the current position used in the buffer
* `start` [`int`]: the offset postition of the directory archive in relation to the start of the file
* `offset` [`int`]: a number to save to current offset position in relation to the start of the directory archive. This value can be `0` if the method is called the first time.
* `buffer` [`bytes`]: obviously the byte buffer of the current file
* `level` [`int`]: used to pretty print the output (do not change this)
* `verbose` [`bool`]: indicate whether the information gathered should be printed
* `@return` the next index and offset values after parsing 
* `@usage`: 
    ```python
    index, _ = isuwalk.isu_parse_entry(tree, index, pos, 0, buffer, verbose=True)
    ```

---
To parse the version string or customisation string in the file header, this function can be used to parse them individually.

    isu_parse_header_name(root, buffer, entry_name, index, verbose = False) -> tuple[int, str]:

* `root` [`FshElement` | `None`]: if the entries in the index of the directory archive should be stored into an object, this parameter should not be `None`.
* `buffer` [`bytes`]: obviously the byte buffer of the current file 
* `entry_name` [`str` | `None`]: when output is enabled or the root element is not null, this element specifies the element.tag and output name.
* `index` [`int`]: the current position used in the buffer
* `verbose` [`bool`]: indicate whether the information gathered should be printed
* `@return` the next index and the parsed name string 
* `@usage`: 
    ```python
    # with root object and verbose
    index, version = isuwalk.isu_parse_header_name(root, buffer, 'Version', index, verbose=True)

    # only parsing
    index, custom = isuwalk.isu_parse_header_name(None, buffer, None, index)
    ```

---
The next method parses a system table entry and stores all information gathered into a `FshElement`.

    isu_parse_table_entry(root, buffer, index, verbose = False, entry_num = 0) -> tuple:

* `root` [`FshElement` | `None`]: if the entries in the index of the directory archive should be stored into an object, this parameter should not be `None`.
* `buffer` [`bytes`]: obviously the byte buffer of the current file 
* `index` [`int`]: the current position used in the buffer
* `verbose` [`bool`]: indicate whether the information gathered should be printed
* `entry_num` [`int`]: the number of the latest entry parsed - the value should be 0 in the beginning
* `@return` the next index, a boolean value that indicates a successfull result and the information packed into an `FshElement`
* `@usage`:     
    ```python
    count = 0
    while buffer[index] != 0x00:
        index, success, element = isuwalk.isu_parse_table_entry(root, buffer, index, verbose, count)
        [...]
    ```

---
In order to parse a field definition the following method can be used:

    isu_parse_buf_or_size(root: FshElement, buffer: bytes, index: int, verbose: bool = False) -> tuple

* `root` [`FshElement` | `None`]: if the entries in the index of the directory archive should be stored into an object, this parameter should not be `None`.
* `buffer` [`bytes`]: obviously the byte buffer of the current file 
* `index` [`int`]: the current position used in the buffer
* `verbose` [`bool`]: indicate whether the information gathered should be printed
* `@return` the next index and a boolean value that indicates a successfull result 
* `@usage`:   
    ```python
    count = 0
    while buffer[index] != 0x20:
        index, success = isuwalk.isu_parse_buf_or_size(root, buffer, index, verbose)
        [...]
    ```

### 3.2 **isu.fsversion**

As described above, this module contains two classes that are used to enumerate the firmware version and customisation. Note that all parameters in the constructors are optional, because a parsing process can be initiated by calling `obj.loads(some_string)`.

---

    class FSCutomization:
        __init__(self, device_type, interface, module_type, module_version)

* `device_type` [`str` | `None`]: usually `ir` for internet radio
* `interface` [`str` | `None`]: The device interface defines how the binary is structured. This API contains an implementation for the `mmi` (Multi Media Interface).
* `module_type` [`str` | `None`]: Additionally, the firmware file structure depends on the used module. (see `fsversion.FSVERSION_MODULE_TYPES` for a list of possible modules) This API puts the focus on `Venice x` modules.
* `module_version` [`str` | `None`]: the version of the used module

---

    class FSVersion:
        __init__(self, firmware_version, sdk_version, revision, branch)
* `firmware_version` [`str` | `None`]: the version of the used firmware
* `sdk_version` [`str` | `None`]: the version of the SDK used to build the firmware. (Info was found [here](https://de.hama.com/webresources/drivers/00054/54818-IR320-Patch-Log.txt))
* `revision` [`str` | `None`]: the revision at the time of publishing this firmware update
* `branch` [`str` | `None`]: this could be the used branch where the software was developed


## 4. Compressed Code

The field `CompSize` defines the size of the first partition included in the firmware file. To extract this specific section of data, the `ISU-Inspector Tool` can be used. It copies the compressed section into a file that is named like the input file plus a `core.bin` extension.

```console
$ python3 isu_inspector.py -if=FILE.isu.bin -e --core --verbose
```
| Idea | Checked | Accepted | Description | 
|:-:|---|---|---|
| Linux Device Tree | True | False | malformed format |
| Master Boot Record | True | False | malformed format, but contains 55 AA  |

    ┌───────────────────────────────────────────────┐
    │ ISU-Core (Compressed)                         │
    ├───────────────────────────────────────────────┤
    │                                               │
    │                                               │
    │                                               │
    │                                               │
    │                                               │
    │                                               │
    │                                               │
    │                                               │
    │                                               │
    │                                ┌──────────────┤
    │                                │ EOF: byte[5] │ 0C 00 11 00 00
    └────────────────────────────────┴──────────────┘
