import struct
from Crypto.Hash import SHA256


class Message:
    """
    https://en.bitcoin.it/wiki/Protocol_documentation#Message_structure
    """
    # Magic values:
    MAIN = 0xD9B4BEF9
    TESTNET = 0xDAB5BFFA
    TESTNET3 = 0x0709110B

    def __init__(self, command, payload, magic=TESTNET3):
        self.command = command.encode('ascii')
        self.payload = bytes.fromhex(payload)
        self.magic = magic.to_bytes(4, byteorder="little")
        self.length = len(self.payload)
        self.checksum = SHA256.new(SHA256.new(self.payload).digest()).digest()[0:4]

    def to_bytes(self):
        return struct.pack('4s12sL4s', self.magic, self.command, self.length, self.checksum) + self.payload