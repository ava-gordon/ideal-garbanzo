import codecs


def hex_encode(var):
    return codecs.encode(var, 'hex_codec')


def hex_decode(var):
    return codecs.decode(var, 'hex_codec')
