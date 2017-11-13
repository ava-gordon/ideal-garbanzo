from lib import generate_address


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


def transaction():
    pass

def main():
    address()

if __name__ == '__main__':
    main()
