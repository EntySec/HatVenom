#!/usr/bin/env python3

#
# MIT License
#
# Copyright (c) 2020-2021 EntySec
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import os


class Macho:
    magic = [
        b"\xca\xfe\xba\xbe",
        b"\xfe\xed\xfa\xce",
        b"\xfe\xed\xfa\xcf",
        b"\xce\xfa\xed\xfe",
        b"\xcf\xfa\xed\xfe"
    ]

    headers = {
        'x64': f'{os.path.dirname(os.path.dirname(__file__))}/templates/macho_x64.bin',
        'aarch64': f'{os.path.dirname(os.path.dirname(__file__))}/templates/macho_aarch64.bin'
    }

    def generated(self, data):
        if data[:4] in self.magic:
            return True
        return False

    def generate(self, arch, data):
        if self.generated(data):
            return data

        if arch in self.headers.keys():
            if os.path.exists(self.headers[arch]):
                data_size = len(data)

                pointer = b'PAYLOAD:'
                pointer_size = len(pointer)

                macho_file = open(self.headers[arch], 'rb')
                macho = macho_file.read()
                macho_file.close()

                pointer_index = macho.index(pointer)

                if data_size >= pointer_size:
                    return macho[:pointer_index] + data + macho[pointer_index + data_size:]
                return macho[:pointer_index] + data + macho[pointer_index + pointer_size:]
        return b''
