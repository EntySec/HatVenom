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

from .exe.pe import PE
from .exe.raw import Raw
from .exe.elf import ELF
from .exe.macho import Macho


class Generator:
    def generate(self, file_format, arch, data, offsets={}):
        if file_format in self.formats.keys():
            for offset in offsets.keys():
                if (':' + offset + ':ip:').encode() in data:
                    data = data.replace((':' + offset + ':ip:').encode(), socket.inet_aton(offsets[offset]))
                elif (':' + offset + ':port:').encode() in data:
                    data = data.replace((':' + offset + ':port:').encode(), struct.pack('>H', int(offsets[offset])))
                elif (':' + offset + ':string:').encode() in data:
                    data = data.replace((':' + offset + ':string:').encode(), offsets[offset].encode())
                elif (':' + offset + ':').encode() in data:
                    sub = offsets[offset] if isinstance(offsets[offset], bytes) else codecs.escape_decode(offsets[offset], 'hex')[0]
                    data = data.replace((':' + offset + ':').encode(), sub)
                else:
                    return b''
            return self.formats[file_format].generate(self, arch, data)
        return b''

    formats = {
        'pe': PE(),
        'raw': Raw(),
        'elf': ELF(),
        'macho': Macho()
    }
