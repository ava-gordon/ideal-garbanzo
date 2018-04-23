import sys
sys.path.append("..")  # So our imports work

from lib.Address.AddressGenerator import AddressGenerator
from lib.Transaction.Transaction import Transaction
from main import make_txin, make_txout


def main():
    address = AddressGenerator()
    txin = make_txin()
    txout = make_txout()
    tx = Transaction([txin], [txout])
    unsigned = tx.to_hex()
    tx.sign(address.priv)
    signed = tx.to_hex()
    print(signed)

if __name__ == "__main__":
    main()