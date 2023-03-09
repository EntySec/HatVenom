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

from .generator import Generator


class HatVenom(Generator):
    """ Main class of hatvenom module.

    This main class of hatvenom module is intended for providing
    implementations of payload generators.
    """

    def __init__(self) -> None:
        super().__init__()

    def generate(self, file_format: str, arch: str, shellcode: bytes) -> bytes:
        """ Generate payload with the specified shellcode.

        :param str file_format: format of the payload executable file
        :param str arch: architecture to generate payload for
        :param bytes shellcode: shellcode to generate payload with
        :return bytes: generated payload
        """

        return self.generate_payload(file_format, arch, shellcode)

    def generate_to(self, file_format: str, arch: str, shellcode: bytes,
                    filename: str = 'a.out') -> None:
        """ Generate payload with the specified shellcode and save it
        to the specified file.

        :param str file_format: format of the payload executable file
        :param str arch: architectyre to generate payload for
        :param bytes shellcode: shellcode to generate payload with
        :param str filename: name of the file to save payload to
        :return None: None
        """

        with open(filename, 'wb') as f:
            f.write(self.generate_payload(file_format, arch, shellcode))
