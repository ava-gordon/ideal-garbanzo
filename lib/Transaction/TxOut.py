

# This is the output of a new transaction. The script_pub_key contains the destination address of this transaction.
class TxOut:
    def __init__(self, value, script_length, script_pub_key):
        self.value = value
        self.script_length = script_length
        self.script_pub_key = script_pub_key

    def to_hex(self):
        pass