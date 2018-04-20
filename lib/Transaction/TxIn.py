

# This is the input for a new transaction. The script_sig contains the signature of the previous UTXO that is being
# spent here.
class TxIn:

    # Explanation: https://bitcoin.stackexchange.com/questions/2025/what-is-txins-sequence
    SEQUENCE_INIT = 0x00000000
    SEQUENCE_LOCKED = 0xffffffff

    # prev_output must be an OutPoint object
    def __init__(self, prev_output, script_length, script_sig):
        self.prev_output = prev_output
        self.script_length = script_length
        self.script_sig = script_sig
        self.sequence = TxIn.SEQUENCE_LOCKED  # For now, let's not bother time-locking transactions

    def to_hex(self):
        pass