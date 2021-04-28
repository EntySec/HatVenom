# HatVenom

Powerful payload generation and shellcode injection tool that provides support for common platforms and architectures.

## Features

* Support for most common executable formats like `elf`, `macho`, `pe`.
* Support for most common architectures like `x64`, `x86`, `aarch64`, `armle`, `mipsle`, `mipsbe`.
* Ability to modify shellcode by changing pre-defined offsets.

## Installation

```bash
git clone https://github.com/EntySec/HatVenom.git
cd HatVenom
sudo python3 setup.py install
```

## Shellcode offsets

Shellcode offsets is a variables used to add something to shelcode on the preprocessing stage. Offsets looks like this:

```
\x90\x90\x90\x90:message:string:\x90\x90\x90\x90
```

Where `message` is an offset name and `string` is an offset type. So the basic usage of the offset looks like:

```
[shellcode]:[name]:[type]:[shellcode]
```

There are some possible offsets types:

* `string` - Plain text that will be converted to bytes on the preprocessing stage.
* `host` - IP address that will be converted to bytes on the preprocessing stage.
* `port` - Numeric port that will be converted to bytes on the preprocessing stage.

So if you want to replace offset with bytes instead of `string`, `host` and `port`, you can use this type:

```
[shellcode]:[name]:[shellcode]
```
