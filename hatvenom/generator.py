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
import sys
import codecs
import argparse
import struct


class PayloadGenerator:
    templates = f'{os.path.dirname(__file__)}/templates/'

    macho_templates = {
        'x64': templates + 'macho_x64.bin',
        'aarch64': templates + 'macho_aarch64.bin'
    }

    @staticmethod
    def ip_to_bytes(host):
        result = b""
        for i in host.split("."):
            result += bytes([int(i)])
        return result

    @staticmethod
    def port_to_bytes(port):
        result = "%.4x" % int(port)
        return bytes.fromhex(result)

    @staticmethod
    def string_to_bytes(string):
        string = string.encode().hex()
        string = '\\x' + '\\x'.join(a + b for a, b in zip(string[::2], string[1::2]))
        return codecs.escape_decode(string, 'hex')[0]

    def generate_payload(self, file_format, arch, data, offsets={}):
        if file_format in self.formats.keys():
            for offset in offsets.keys():
                if (':' + offset + ':ip:').encode() in data:
                    data = data.replace((':' + offset + ':ip:').encode(), self.ip_to_bytes(offsets[offset]))
                elif (':' + offset + ':port:').encode() in data:
                    data = data.replace((':' + offset + ':port:').encode(), self.port_to_bytes(offsets[offset]))
                elif (':' + offset + ':string:').encode() in data:
                    data = data.replace((':' + offset + ':string:').encode(), self.string_to_bytes(offsets[offset]))
                elif (':' + offset + ':').encode() in data:
                    sub = offsets[offset] if isinstance(offsets[offset], bytes) else codecs.escape_decode(offsets[offset], 'hex')[0]
                    data = data.replace((':' + offset + ':').encode(), sub)
                else:
                    return None
            return self.formats[file_format](self, arch, data)
        return None

    def generate_macho(self, arch, data):
        if arch in self.macho_templates.keys():
            if os.path.exists(self.macho_templates[arch]):
                if len(data) >= len('PAYLOAD:'):
                    macho_file = open(self.macho_templates[arch], 'rb')
                    macho = macho_file.read()
                    macho_file.close()

                    payload_index = macho.index(b'PAYLOAD:')
                    content = macho[:payload_index] + data + macho[payload_index + len(data):]
                    return content
        return None

    def generate_raw(self, arch, data):
        if arch in ['generic']:
            return data
        return None

    formats = {
        'pe': generate_pe,
        'elf': generate_elf,
        'macho': generate_macho,
        'raw': generate_raw
    }
