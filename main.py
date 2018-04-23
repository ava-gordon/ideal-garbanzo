from lib.Address.AddressGenerator import AddressGenerator
from lib.Transaction.TxOut import TxOut
from lib.Transaction.TxIn import TxIn
from lib.Transaction.Transaction import Transaction

# todo: make amount to send configurable
# todo: auto-generate "change" output to send remaining balance back to sender
# todo: CLI - need to be able to see balance, create transactions
# todo: storing user info - private keys, balances, etc.
# todo: verifying balances with blockchain.info or some other provider (don't want to DL the whole chain)
# todo: standardize which variable types are passed around (strings vs. hex)
# todo: unit tests


def gen_address():
    address = AddressGenerator()
    print(address.pub)


# need some way of storing tx info
def transaction():
    txin = make_txin()
    txout = make_txout()

    return Transaction([txin], [txout])


# A couple of helper functions for early testing - will remove these hardcoded values
def make_txin():
    address = AddressGenerator()
    utxo_hash = "79fa40d08954eca683689b0fdcbdd7b1b5c2678f42ebc38309dd282334067f86"
    return TxIn.generate_unsigned_txin(utxo_hash, 0, address.addr)


def make_txout():
    # let's default to sending our test btc's back to the testnet faucet where we got them in the first place.
    testnet_faucet_address = "2N8hwP1WmJrFF5QWABn38y63uYLhnJYJYTF"
    value = 1.8 * 10**8  # currently generated address has one utxo with this amount
    value = int(value)
    return TxOut(value, testnet_faucet_address)


def main():
    pass

if __name__ == '__main__':
    main()
