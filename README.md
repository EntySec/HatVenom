# HatVenom

Powerful payload generation and shellcode injection tool that provides support for common platforms and architectures.

## CLI examples

```bash
python3 hatvenom.py --format elf --arch x64 --shellcode '\x90\x90\x90'
```

## Python example

```python
from core.hatvenom import HatVenom

hatvenom = HatVenom()
hatvenom.generate_to('elf', 'x64', b'\x90\x90\x90', '/tmp/payload.bin')
```
