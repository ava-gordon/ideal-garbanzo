import ecdsa
import base58
import codecs
import Crypto.Random as rand
from Crypto.Hash import SHA256, RIPEMD160

"""
As with everything in Bitcoin, the technicals of generating a bitcoin address are quite complicated. 
More details as to what's happening in this file can be found here:
https://en.bitcoin.it/wiki/Technical_background_of_version_1_Bitcoin_addresses#How_to_create_Bitcoin_Address
"""

ADDRESS_VERSION_TESTNET = 0x6F
ADDRESS_VERSION_MAINNET = 0x00


class AddressGenerator:

    def __init__(self, secret=b'this is my secret, get your own!', debug=False):
        self.debug = debug  # todo: define a logger to handle this
        self.priv = self._generate_private_key_from_secret(secret)
        self.pub = self._generate_public_key(self.priv)
        self.wif = self._wif_private_key(self.priv)
        self.addr = self._generate_address_from_public_key(self.pub)

        if debug:
            print('private key: ' + str(self.priv))
            print('public key: ' + str(self.pub))
            print('WIF key: ' + str(self.wif))
            print('address: ' + str(self.addr))

    def _generate_private_key(self):
        bits = rand.get_random_bytes(32)
        return codecs.encode(bits, 'hex_codec')

    def _generate_private_key_from_secret(self, secret):
        bits = SHA256.new(secret).digest()
        return codecs.encode(bits, 'hex_codec')

    def _wif_private_key(self, private_key):
        return base58.b58encode_check(private_key)

    def _generate_public_key(self, private_key):
        pk_string = codecs.decode(private_key, 'hex_codec')
        sk = ecdsa.SigningKey.from_string(pk_string, curve=ecdsa.SECP256k1)
        vk = sk.get_verifying_key()
        return codecs.encode(b'\x04', 'hex_codec') + codecs.encode(vk.to_string(), 'hex_codec')

    def _generate_address_from_public_key(self, public_key):
        hash = RIPEMD160.new(SHA256.new(codecs.decode(public_key, 'hex_codec')).digest()).digest()
        hash = bytes([ADDRESS_VERSION_TESTNET]) + hash
        return base58.b58encode_check(hash)
