"""
MIT License

Copyright (c) 2020-2023 EntySec

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import argparse
import codecs
import sys

from .badges import Badges
from .generator import Generator


class HatVenomCLI(Generator, Badges):
    """ Subclass of hatvenom module.

    This subclass of hatvenom module is intended for providing
    command-line interface for HatVenom.
    """

    def __init__(self) -> None:
        super().__init__()

        self.description = (
            'HatVenom is a powerful payload generation tool that provides support'
            ' for all common platforms and architectures.'
        )

        self.parser = argparse.ArgumentParser(description=self.description)
        self.parser.add_argument('-f', '--format', dest='format', help='Platform to generate for.')
        self.parser.add_argument('-a', '--arch', dest='arch', help='Architecture to generate for.')
        self.parser.add_argument('-s', '--shellcode', dest='shellcode', help='Shellcode to inject.')
        self.parser.add_argument('-o', '--output', dest='output', help='File to output generated payload.')
        self.args = self.parser.parse_args()

    def start(self) -> None:
        """ Main command-line arguments handler.

        :return None: None
        """

        if self.args.output:
            directory = os.path.split(self.args.output)[0]
            if not os.path.isdir(directory):
                self.print_error(f"Directory: {directory}: does not exist!")
                return

        if self.args.format and self.args.arch and self.args.shellcode:
            filename = self.args.output if self.args.output else 'a.out'
            shellcode = codecs.escape_decode(self.args.shellcode, 'hex')[0]

            self.print_process("Generating payload...")
            payload = self.generate_payload(self.args.format, self.args.arch, shellcode)

            if payload is None:
                self.print_error(f"Invalid format or architecture specified!")
                return

            self.print_information(f"Final payload size: {str(len(payload))}")
            self.print_process(f"Saving payload to {filename}...")

            with open(filename, 'wb') as f:
                f.write(payload)

            self.print_success(f"Payload saved to {filename}!")
        else:
            self.parser.print_help()


def main() -> None:
    """ HatVenom command-line interface.

    :return None: None
    """

    try:
        cli = HatVenomCLI()
        cli.start()
    except Exception:
        pass
