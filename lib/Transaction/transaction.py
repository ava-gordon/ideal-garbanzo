
class Transaction:

    VERSION = 0x01000000
    FLAG = 0x0001

    def __init__(self, tx_in_list, tx_out_list, lock_time = 0, segwit = False):
        self.version = Transaction.VERSION
        self.tx_in_count = len(tx_in_list)
        self.tx_in_list = tx_in_list
        self.tx_out_count = len(tx_out_list)
        self.tx_out_list = tx_out_list
        self.lock_time = lock_time

        # no segwit for the moment
        if (segwit):
            self.flag = Transaction.FLAG
            self.witnesses = []

    def to_hex(self):
        pass