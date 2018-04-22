

# This is the output of a new transaction. The script_pub_key contains the destination address of this transaction.
class TxOut:
    def __init__(self, value, script_length, script_pub_key):
        """
        
        :param value: an int representing the number of SATOSHIS (not btc) 
        :param script_length: 
        :param script_pub_key: 
        """
        self.value = value.to_bytes(8, byteorder="little")
        self.script_length = script_length
        self.script_pub_key = script_pub_key

    def to_hex(self):
        return "{}{}{}".format(self.value.hex(), "", "")  # leave script length and pub key blank until we handle signing transactions