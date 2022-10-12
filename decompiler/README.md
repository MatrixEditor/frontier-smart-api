# ECMAScript-Decompiler

![Status](https://img.shields.io:/static/v1?label=Status&message=LAST-STAGE&color=grey)
![Platform](https://img.shields.io:/static/v1?label=Platforms&message=UNIX|Windows&color=yellowgreen)

Frontier Smart products with the `FS2028` (`Venice 8`) module store a different directory archive. It contains compiled ECMAScript files (`es.bin`) and some graphic resources for the device's display. 

The binary files contains XDR bytes code from the `SpiderMonkey` JavaScript-Engine on version `1.8`, which is very old. The decompiler script provided here can be used to decompile the binary files stored in the directory archives. 

### Usage

````sh
$ ./ecma-decompiler xdrfile.es.bin > decompiled_output.js
````

To compile it from source, you will need the [SpiderMonkey 1.8](http://ftp.mozilla.org/pub/mozilla.org/js/js-1.8.0-rc1.tar.gz) release, which is currently available at the official Mozilla server. When working with Windows, it is almost impossible to compile the source code, because it requires the Microsoft Visual Studio 97 edition (5.0). 

