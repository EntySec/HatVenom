#!/usr/bin/env python3

#
# MIT License
#
# Copyright (c) 2020-2022 EntySec
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


class Dll:
    magic = [
        b"\x4d\x5a"
    ]

    headers = {
        'x64': f'{os.path.dirname(os.path.dirname(__file__))}/templates/dll/dll_x64.dll',
        'x86': f'{os.path.dirname(os.path.dirname(__file__))}/templates/dll/dll_x86.dll'
    }

    def generated(self, data):
        if data[:2] in self.magic:
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

                with open(self.headers[arch], 'rb') as dll_file:
                    dll = dll_file.read()
                    pointer_index = dll.index(pointer)

                    if data_size >= pointer_size:
                        return dll[:pointer_index] + data + dll[pointer_index + data_size:]
                    return dll[:pointer_index] + data + dll[pointer_index + pointer_size:]
        return b''
