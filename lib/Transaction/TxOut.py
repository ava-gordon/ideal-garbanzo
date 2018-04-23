from .ScriptPubKey import default_script_pub_key
from ..utils.VarInt import VarInt


# This is the output of a new transaction. The script_pub_key contains the destination address of this transaction.
class TxOut:
    def __init__(self, value, address):
        """
        
        :param value: an int representing the number of SATOSHIS (not btc) 
        :param address: a bitcoin address
        """
        self.value = value.to_bytes(8, byteorder="little")
        self.script_pub_key = default_script_pub_key(address)
        self.script_length = VarInt(len(self.script_pub_key)/2)

    def to_hex(self):
        return "{}{}{}".format(self.value.hex(), self.script_length.to_hex(), self.script_pub_key)  # leave script length and pub key blank until we handle signing transactions