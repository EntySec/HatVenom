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

from pex.socket import Socket

from .exe import Exe


class Generator(Socket, Exe):
    @staticmethod
    def detect_endian(arch):
        if arch.endswith('be'):
            return 'big'
        return 'little'

    def generate_payload(self, file_format, arch, data, offsets={}):
        if file_format is None or file_format in self.exe_formats.keys():
            for offset in offsets.keys():
                if (':' + offset + ':ip:').encode() in data:
                    offset_code = (':' + offset + ':ip:').encode()
                    data = self.replace_offset(
                        file_format,
                        offset_code,
                        data,
                        self.pack_host(
                            offsets[offset],
                            self.detect_endian(arch)
                        )
                    )

                elif (':' + offset + ':port:').encode() in data:
                    offset_code = (':' + offset + ':port:').encode()
                    data = self.replace_offset(
                        file_format,
                        offset_code,
                        data,
                        self.pack_port(
                            offsets[offset],
                            self.detect_endian(arch)
                        )
                    )

                elif (':' + offset + ':string:').encode() in data:
                    offset_code = (':' + offset + ':string:').encode()
                    data = self.replace_offset(
                        file_format,
                        offset_code,
                        data,
                        offsets[offset].encode()
                    )

                elif (':' + offset + ':').encode() in data:
                    offset_code = (':' + offset + ':').encode()

                    if isinstance(offsets[offset], bytes):
                        content = offsets[offset]
                    else:
                        content = offsets[offset].encode()

                    data = self.replace_offset(
                        file_format,
                        offset_code,
                        data,
                        content
                    )

                else:
                    return b''

            if file_format is None:
                return data

            return self.exe_formats[file_format].generate(arch, data)
        return b''

    def replace_offset(self, file_format, offset, data, content):
        if self.exe_formats[file_format].generated(data):
            content_size = len(content)
            offset_size = len(offset)

            offset_index = data.index(offset)

            if content_size >= offset_size:
                return data[:offset_index] + content + data[offset_index + content_size:]
            return data[:offset_index] + content + data[offset_index + offset_size:]

        return data.replace(offset, content)
