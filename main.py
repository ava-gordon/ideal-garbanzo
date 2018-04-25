from lib.Address.AddressGenerator import AddressGenerator
from lib.Transaction.TxOut import TxOut
from lib.Transaction.TxIn import TxIn
from lib.Transaction.Transaction import Transaction
from lib.Network.NetworkHandler import NetworkHandler

# todo 1: send transaction to network
# todo 2: make amount to send configurable
# todo 3: auto-generate "change" output to send remaining balance back to sender
# todo 4: CLI - need to be able to see balance, create transactions
# todo 5: storing user info - private keys, balances, etc.
# todo 6: verifying balances with blockchain.info or some other provider (don't want to DL the whole chain)
# todo 7: standardize which variable types are passed around (strings vs. hex)
#  Current thinking here: Always pass everything as hex strings, convert to bytes only as necessary
# todo 8: unit tests
# todo: Move to virtualenv
# todo: Install LOC counter


def gen_address():
    address = AddressGenerator()
    print(address.pub)


# need some way of storing tx info
def transaction():
    txin = make_txin()
    txout = make_txout()

    return Transaction([txin], [txout])

def find_peer():
    nw_handler = NetworkHandler()

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
