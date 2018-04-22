

class OutPoint:
    def __init__(self, hash, index):
        self.hash = hash
        self.index = index

        if not isinstance(self.index, bytes):
            self.index = self.index.to_bytes(4, byteorder="big")

        if not isinstance(self.hash, bytes):
            self.hash = OutPoint._tx_hash_from_hash_string(self.hash)

    def to_hex(self):
        return "{}{}".format(self.hash.hex(), self.index.hex())

    @staticmethod
    def _tx_hash_from_hash_string(hash_string):
        hash_rev = hash_string[::-1]
        h = bytes.fromhex(hash_rev)
        return h
