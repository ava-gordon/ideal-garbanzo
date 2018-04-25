from lib.utils.VarInt import VarInt


class VarStr:
    """
    https://en.bitcoin.it/wiki/Protocol_documentation#Variable_length_string
    """

    def __init__(self, string):
        # Could just call set_string here, but it's considered good practice to define all instance vars in __init__()
        self.string = string
        self.length = VarInt(len(string))

    def set_string(self, string):
        self.string = string
        self.length = VarInt(len(string))

    def to_hex(self):
        return "{}{}".format(self.length.to_hex(), self.string)
