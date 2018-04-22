import codecs
from ..utils.VarInt import VarInt


class Transaction:

    VERSION = '01000000'
    FLAG = '0001'
    LOCK_TIME = '00000000'

    def __init__(self, tx_in_list, tx_out_list, lock_time=0):
        self.version = Transaction.VERSION
        self.tx_in_count = VarInt(len(tx_in_list))
        self.tx_in_list = tx_in_list
        self.tx_out_count = VarInt(len(tx_out_list))
        self.tx_out_list = tx_out_list
        self.lock_time = lock_time

        # no segwit for the moment
        # if segwit:
        #     self.flag = Transaction.FLAG
        #     self.witnesses = []

    def to_hex(self):
        tx_in_string = ''.join([tx_in.to_hex() for tx_in in self.tx_in_list])
        tx_out_string = ''.join([tx_out.to_hex() for tx_out in self.tx_out_list])
        return (
            self.version +
            self.tx_in_count.to_hex() +
            tx_in_string +
            self.tx_out_count.to_hex() +
            tx_out_string +
            Transaction.LOCK_TIME  # for the moment, no block locking - ignore inputted lock time
        )

