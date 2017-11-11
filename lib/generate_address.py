import ecdsa
import base58
import codecs
import Crypto.Random as rand
from Crypto.Hash import SHA256, RIPEMD160


def generate_private_key():
    bits = rand.get_random_bytes(32)
    print(bits)
    return codecs.encode(bits, 'hex_codec')

def WIF_private_key(private_key):
    return base58.b58encode(private_key)

def generate_public_key(private_key):
    pk_string = codecs.decode(private_key, 'hex_codec')
    sk = ecdsa.SigningKey.from_string(pk_string, curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    return codecs.encode(b'\x04', 'hex_codec') + codecs.encode(vk.to_string(), 'hex_codec')

def generate_address_from_public_key(public_key):
    hash = RIPEMD160.new(SHA256.new(codecs.decode(public_key, 'hex_codec')).digest())
    return base58.b58encode(hash.digest())

def generate_address_from_private_key(private_key):
    return generate_address_from_public_key(generate_public_key(private_key))