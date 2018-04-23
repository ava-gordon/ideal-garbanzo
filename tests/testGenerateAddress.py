import sys
sys.path.append("..")  # So our imports work
import codecs
from lib.Address.AddressGenerator import AddressGenerator

def main():
    address = AddressGenerator()
    pub = codecs.decode(address.pub, 'hex_codec')
    print(pub)
    print(pub.hex())
    print(address.addr == "mkjvqevmHTHo2XF5wDLK9E9jefzDeJ9APh")


if __name__ == "__main__":
    main()