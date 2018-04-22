from lib import generate_address
from lib.Transaction.transaction import Transaction
from lib.Transaction.TxIn import TxIn
from lib.Transaction.TxOut import TxOut
from lib.Transaction.OutPoint import OutPoint


def address():
    priv = generate_address.generate_private_key_from_secret()
    print('private key: ' + str(priv))
    pub = generate_address.generate_public_key(priv)
    print('public key: ' + str(pub))
    wif = generate_address.wif_private_key(priv)
    print('WIF key: ' + str(wif))
    addr = generate_address.generate_address_from_public_key(pub)
    addr2 = generate_address.generate_address_from_private_key(priv)
    print('address from pub: ' + str(addr))
    print('address from priv: ' + str(addr2))


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
    address()

if __name__ == '__main__':
    main()
