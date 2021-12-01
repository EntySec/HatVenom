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


class XOR:
    def encode(self, shellcode, decode=False):
        shellcode = bytearray(shellcode)

        if decode:
            shellcode.reverse()
            encoded_payload = bytearray()

            for i, byte in enumerate(shellcode):
                if i == len(shellcode) - 1:
                    encoded_payload.append(shellcode[i])
                else:
                    encoded_payload.append(shellcode[i] ^ shellcode[i + 1])

            encoded_payload.reverse()
        else:
            encoded_payload = bytearray([shellcode.pop(0)])

            for i, byte in enumerate(shellcode):
                encoded_payload.append(byte ^ encoded_payload[i])

        return bytes(encoded_payload)
