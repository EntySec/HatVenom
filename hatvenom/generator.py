"""
MIT License

Copyright (c) 2020-2023 EntySec

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from pex.exe import *


class Generator(PE, ELF, DLL, Macho, Dylib):
    """ Subclass of hatvenom module.

    This subclass of hatvenom module is intended for providing
    an implementation of a native executable files generator.
    """

    def __init__(self) -> None:
        super().__init__()

    def generate_payload(self, file_format: str, arch: str, data: bytes) -> bytes:
        """ Generate executable file with the specified data.

        :param str file_format: executable file format
        :param str arch: architecture to generate executable for
        :param bytes data: data to generate executable with
        :return bytes: generated executable
        """

        if file_format == 'pe':
            return self.pack_pe(arch, data)

        if file_format == 'elf':
            return self.pack_elf(arch, data)

        if file_format == 'dll':
            return self.pack_dll(arch, data)

        if file_format == 'macho':
            return self.pack_macho(arch, data)

        if file_format == 'dylib':
            return self.pack_dylib(arch, data)
