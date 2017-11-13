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

def generate_private_key():
    bits = rand.get_random_bytes(32)
    return codecs.encode(bits, 'hex_codec')


def generate_private_key_from_secret():
    bits = SHA256.new(b'this is my secret, get your own!').digest() 
    return codecs.encode(bits, 'hex_codec')


def wif_private_key(private_key):
    return base58.b58encode_check(private_key)


def generate_public_key(private_key):
    pk_string = codecs.decode(private_key, 'hex_codec')
    sk = ecdsa.SigningKey.from_string(pk_string, curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    return codecs.encode(b'\x04', 'hex_codec') + codecs.encode(vk.to_string(), 'hex_codec')


def generate_address_from_public_key(public_key):
    hash = RIPEMD160.new(SHA256.new(codecs.decode(public_key, 'hex_codec')).digest()).digest()
    hash = bytes([ADDRESS_VERSION_TESTNET]) + hash
    return base58.b58encode_check(hash)


def generate_address_from_private_key(private_key):
    return generate_address_from_public_key(generate_public_key(private_key))