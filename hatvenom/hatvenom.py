from .generator import PayloadGenerator

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
