import ecdsa
import codecs


def public_key_from_private_key(private_key):
    """
    :param private_key: A bytes object containing the private key
    :return: 
    """
    sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    return codecs.encode(vk.to_string(), 'hex_codec')