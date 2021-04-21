#!/usr/bin/env python3

import sys
import argparse

from core.payload import PayloadGenerator

parser = argparse.ArgumentParser()
parser.add_argument('--format', dest='format', help='Platform to generate for.')
parser.add_argument('--architeture', dest='architecture', help='Architecture to generate for.')
parser.add_argument('--shellcode', dest='shellcode', help='Shellcode to inject.')
parser.add_argument('-o', '--output', dest='output', help='File to output generated payload.')
args = parser.parse_args()

if __name__ == '__main__':
    if args.format and args.architecture:
        pg = PayloadGenerator()
        shellcode = bytes(args.shellcode) if args.shellcode else b'\x00'
        filename = args.output if args.output else 'a.out'

        print("[*] Generating payload...")
        payload = pg.generate(args.format, args.architecture, bytes(args.shellcode))
        print(f"[i] Final payload size: {str(len(payload))}")

        print(f"[*] Saving payload to {filename}...")
        with open(filename, 'wb') as f:
            f.write(payload)
        print(f"[+] Payload saved to {filename}!")
        sys.exit(1)
    else:
        print("[-] No format and architecture specified!")

    print("[-] Failed to generate payload!")
    sys.exit(1)
