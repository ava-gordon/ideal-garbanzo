from .OutPoint import OutPoint
from .ScriptPubKey import default_script_pub_key
from ..utils.VarInt import VarInt


class TxIn:

    # Explanation: https://bitcoin.stackexchange.com/questions/2025/what-is-txins-sequence
    SEQUENCE_INIT = "00000000"
    SEQUENCE_LOCKED = "ffffffff"

    # prev_output must be an OutPoint object
    def __init__(self, prev_output, script_sig):
        """
        
        :param prev_output: an OutPoint object
        :param script_sig: a bitcoin script in hex string format
        """
        self.prev_output = prev_output
        self.script_sig = script_sig  # Unlocks a previous output
        self.script_length = VarInt(int(len(self.script_sig) / 2))
        self.sequence = TxIn.SEQUENCE_LOCKED  # For now, let's not bother time-locking transactions

    def to_hex(self):
        return "{}{}{}{}".format(self.prev_output.to_hex(), self.script_length.to_hex(), self.script_sig,
                                 self.sequence)

    def human_readable(self):
        return "previous output: {} \n script length: {} \n script: {} \n sequence: {}"\
            .format(self.prev_output.to_hex(), self.script_length.to_hex(), self.script_sig, self.sequence)

    def set_script_sig(self, script_sig):
        self.script_sig = script_sig
        self.script_length = VarInt(int(len(self.script_sig) / 2))

    @classmethod
    def generate_u_txins(cls, hashes, address):
        txins = []
        for i in range(len(hashes)):
            hash = hashes[i]
            txin = cls.generate_unsigned_txin(hash, i, address)
            txins.append(txin)
        return txins

    @classmethod
    def generate_unsigned_txin(cls, hash, index, address):
        """
        Generating TxIns is tricky, since the scriptSig itself contains a hash of the Transaction we're creating. 
        To get around this, we do the following: 
        1. Temporarily fill the TxIn with the scriptPubKey that we'll use for our TxOuts. Normally, we'd grab the actual
            scriptPubKeys of the utxo's that are being used as inputs, but instead of that, we will assume that it's the 
            default, since we currently don't have the blockchain downloaded. Note that this means that this wallet
            will not work with nonstandard transactions. 
            
        2. Create the signature of this Transaction with our private key 
        
        3. Replace the scriptSig in the TxIns with the correct signature information
        
        :param hash: The hash of the utxo being used as an input
        :param index: The index of the txin in this transaction's list of txins as an integer
        :param address: The address of the sender of the current transaction 
        :return: 
        """
        outpoint = OutPoint(hash, index)

        # here we are assuming that all the utxo's being used as inputs are standard transactions
        # addressed to the sender
        script_sig = default_script_pub_key(address)

        return cls(outpoint, script_sig)
