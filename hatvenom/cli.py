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

import sys
import codecs
import argparse

from .generator import PayloadGenerator
from .badges import Badges


class StoreDictKeyPair(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        my_dict = {}
        for kv in values.split(","):
            k, v = kv.split("=")
            my_dict[k] = v
        setattr(namespace, self.dest, my_dict)


class HatVenomCLI(PayloadGenerator, Badges):
    description = "Powerful payload generation and shellcode injection tool that provides support for common platforms and architectures."
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--format', dest='format', help='Platform to generate for.')
    parser.add_argument('--arch', dest='arch', help='Architecture to generate for.')
    parser.add_argument('--shellcode', dest='shellcode', help='Shellcode to inject.')
    parser.add_argument('--offsets', dest='offsets', help='Shellcode offsets.', action=StoreDictKeyPair)
    parser.add_argument('-o', '--output', dest='output', help='File to output generated payload.')
    parser.add_argument('-l', '--list', action="store_true", help='List all formats and platforms.')
    args = parser.parse_args()

    def start(self):
        if self.args.list:
            formats = ""
            print(formats)
            sys.exit(0)

        if self.args.format and self.args.arch and self.args.shellcode:
            offsets = dict() if not self.args.offsets else self.args.offsets

            filename = self.args.output if self.args.output else 'a.out'
            shellcode = codecs.escape_decode(self.args.shellcode, 'hex')[0]

            self.print_process("Generating payload...")
            payload = self.generate_payload(self.args.format, self.args.arch, shellcode, offsets)

            if payload is None:
                self.print_error(f"[-] Invalid format or architecture specified!")
                sys.exit(1)

            self.print_information(f"Final payload size: {str(len(payload))}")
            self.print_process(f"Saving payload to {filename}...")

            with open(filename, 'wb') as f:
                f.write(payload)

            self.print_success(f"Payload saved to {filename}!")
            sys.exit(0)
        else:
            self.print_error("No format, architecture and shellcode specified!")

        self.print_error("Failed to generate payload!")
        sys.exit(1)

def main():
    cli = HatVenomCLI()
    cli.start()
