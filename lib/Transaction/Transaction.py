import ecdsa
import base58
import codecs
import Crypto.Random as rand
from Crypto.Hash import SHA256, RIPEMD160
from ..utils.VarInt import VarInt
from ..utils.Keys import public_key_from_private_key


class Transaction:
    """
    https://en.bitcoin.it/wiki/Protocol_documentation#tx
    """

    VERSION = '01000000'
    FLAG = '0001'
    LOCK_TIME = '00000000'
    HASH_CODE = '01000000'

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

    def human_readable(self):
        print("txins: {}\n".format([txin.human_readable() for txin in self.tx_in_list], []))

    def sign(self, private_key):
        """
        Called once the fully serialized, unsigned transaction (with placeholder scriptSig) is created
        :param private_key: The bytes of the private key, encoded in hex as normal
        :return: 
        """

        tx_hex = self.to_hex() + self.HASH_CODE
        tx_bytes = bytes.fromhex(tx_hex)
        hash_obj = SHA256.new(SHA256.new(tx_bytes).digest()).digest()  # SHA256 that biiiih twice

        # sign the transaction with the user's private key, output is in DER encoding
        private_key = codecs.decode(private_key, 'hex_codec')  # We have to decode from hex before signing
        signing_key = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
        sig = signing_key.sign_digest(hash_obj, sigencode=ecdsa.util.sigencode_der) + int(1).to_bytes(1, byteorder="big")

        # this is the same as the user's public key
        # need to do some finagling to get this into the proper encoding in the final output
        # See my to do note in main.py about standardizing formats
        public_key = codecs.decode(public_key_from_private_key(private_key), 'hex_codec')

        script_sig = int(len(sig)).to_bytes(1, byteorder="big").hex() \
                     + sig.hex() \
                     + int(len(public_key)).to_bytes(1, byteorder="big").hex() \
                     + public_key.hex()

        for tx in self.tx_in_list:
            tx.set_script_sig(script_sig)
