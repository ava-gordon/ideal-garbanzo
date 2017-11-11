

class TxIn:

    SEQUENCE_INIT   = 0x00000000
    SEQUENCE_LOCKED = 0xffffffff

    # prev_output must be an OutPoint object
    def __init__(self, prev_output, script_length, script):
        self.prev_output = prev_output
        self.script_length = script_length
        self.script = script
        self.sequence = TxIn.SEQUENCE_LOCKED

    def to_hex(self):
        pass