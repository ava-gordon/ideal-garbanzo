from lib.Address.AddressGenerator import AddressGenerator
from lib.Transaction.TxOut import TxOut
from lib.Transaction.TxIn import TxIn
from lib.Transaction.transaction import Transaction


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
    utxo_hash = "79fa40d08954eca683689b0fdcbdd7b1b5c2678f42ebc38309dd282334067f86"
    return TxIn.generate_txin(utxo_hash, 0)


def make_txout():
    value = 1.8 * 10**8  # currently generated address has one utxo
    value = int(value)
    return TxOut(value, 0, "")



def main():
    pass

if __name__ == '__main__':
    main()
