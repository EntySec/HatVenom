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

from core.payload import PayloadGenerator

description = "Powerful payload generation and shellcode injection tool that provides support for common platforms and architectures."
parser = argparse.ArgumentParser(description=description)
parser.add_argument('--format', dest='format', help='Platform to generate for.')
parser.add_argument('--arch', dest='arch', help='Architecture to generate for.')
parser.add_argument('--shellcode', dest='shellcode', help='Shellcode to inject.')
parser.add_argument('-o', '--output', dest='output', help='File to output generated payload.')
args = parser.parse_args()

if __name__ == '__main__':
    if args.format and args.arch and args.shellcode:
        pg = PayloadGenerator()
        filename = args.output if args.output else 'a.out'
        shellcode = codecs.escape_decode(args.shellcode, 'hex')[0]

        print(f"[i] Target format: {args.format}")
        print(f"[i] Target architecture: {args.arch}")

        print("[*] Generating payload...")
        payload = pg.generate(args.format, args.arch, shellcode)

        if payload is None:
            print(f"[-] Invalid format or architecture specified!")
            sys.exit(1)

        print(f"[i] Final payload size: {str(len(payload))}")
        print(f"[*] Saving payload to {filename}...")
        with open(filename, 'wb') as f:
            f.write(payload)
        print(f"[+] Payload saved to {filename}!")
        sys.exit(0)
    else:
        print("[-] No format, architecture and shellcode specified!")

    print("[-] Failed to generate payload!")
    sys.exit(1)
