import base58
from ..utils.VarInt import VarInt

# Let's define some Script opcode constants. just the ones we need for a basic default tx
OP_DUP         = "76"
OP_HASH160     = "a9"
OP_EQUALVERIFY = "88"
OP_CHECKSIG    = "ac"


def default_script_pub_key(address):
    # convert the address to hex, leaving off the checksum and version flag
    address = base58.b58decode_check(address)[2:]
    address_length = VarInt(len(address)/2)
    return "{}{}{}{}{}{}".format(OP_DUP,
                                 OP_HASH160,
                                 address_length.to_hex(),
                                 address,
                                 OP_EQUALVERIFY,
                                 OP_CHECKSIG)


