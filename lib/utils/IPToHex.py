
def ipv4ToHex(ip):
    ip_segments = ip.split(".")
    out = ""
    for segment in ip_segments:
        out += int(segment).to_bytes(2, byteorder="big").hex()

    return out
