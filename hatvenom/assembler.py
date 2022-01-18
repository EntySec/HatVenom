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

import keystone


class Assembler:
    architectures = {
        'x86': [keystone.KS_ARCH_X86, keystone.KS_MODE_32],
        'x64': [keystone.KS_ARCH_X86, keystone.KS_MODE_64],

        'aarch64': [keystone.KS_ARCH_ARM64, 0],
        'armle': [keystone.KS_ARCH_ARM, keystone.KS_MODE_ARM + keystone.KS_MODE_LITTLE_ENDIAN],
        'armbe': [keystone.KS_ARCH_ARM, keystone.KS_MODE_ARM + keystone.KS_MODE_BIG_ENDIAN],

        'mips64le': [keystone.KS_ARCH_MIPS, keystone.KS_MODE_MIPS64 + keystone.KS_MODE_LITTLE_ENDIAN],
        'mips64be': [[keystone.KS_ARCH_MIPS, keystone.KS_MODE_MIPS64 + keystone.KS_MODE_BIG_ENDIAN]],
        'mipsle': [keystone.KS_ARCH_MIPS, keystone.KS_MODE_MIPS32 + keystone.KS_MODE_LITTLE_ENDIAN],
        'mipsbe': [keystone.KS_ARCH_MIPS, keystone.KS_MODE_MIPS32 + keystone.KS_MODE_BIG_ENDIAN]
    }

    def assemble_code(self, arch, code, mode=None):
        if arch in self.architectures:
            target = self.architectures[arch]

            if arch == 'armle' and mode == 'thumb':
                target[1] = keystone.KS_MODE_THUMB + keystone.KS_MODE_LITTLE_ENDIAN
            elif arch == 'armbe' and mode == 'thumb':
                target[1] = keystone.KS_MODE_THUMB + keystone.KS_MODE_BIG_ENDIAN

            ks = keystone.Ks(*target)
            machine = ks.asm(code.encode())

            if machine:
                return bytes(machine[0])
        return b''
