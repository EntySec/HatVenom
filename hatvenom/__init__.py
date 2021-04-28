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
import codecs




class HatVenom(PayloadGenerator):
    def ip_bytes(self, ip):
        return self.ip_to_bytes(ip)

    def port_bytes(self, port):
        return self.port_to_bytes(port)

    def string_bytes(self, string):
        return self.string_to_bytes(string)

    def generate(self, file_format, arch, shellcode, offsets={}):
        return self.generate_payload(file_format, arch, shellcode, offsets)

    def generate_to(self, file_format, arch, shellcode, offsets={}, filename='a.out'):
        with open(filename, 'wb') as f:
            f.write(self.generate_payload(file_format, arch, shellcode, offsets))


class StoreDictKeyPair(argparse.Action):
     def __call__(self, parser, namespace, values, option_string=None):
         my_dict = {}
         for kv in values.split(","):
             k,v = kv.split("=")
             my_dict[k] = v
         setattr(namespace, self.dest, my_dict)


class HatVenomCLI(PayloadGenerator):
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

            print(f"[i] Target format: {self.args.format}")
            print(f"[i] Target architecture: {self.args.arch}")

            print("[*] Generating payload...")
            payload = self.generate_payload(self.args.format, self.args.arch, shellcode, offsets)

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
