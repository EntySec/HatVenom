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

            print("Generating payload...")
            payload = self.generate_payload(self.args.format, self.args.arch, shellcode, offsets)

            if payload is None:
                print(f"[-] Invalid format or architecture specified!")
                sys.exit(1)

            print(f"Final payload size: {str(len(payload))}")
            print(f"Saving payload to {filename}...")
            with open(filename, 'wb') as f:
                f.write(payload)
            print(f"Payload saved to {filename}")
            sys.exit(0)
        else:
            print("No format, architecture and shellcode specified.")

        print("Failed to generate payload.")
        sys.exit(1)
