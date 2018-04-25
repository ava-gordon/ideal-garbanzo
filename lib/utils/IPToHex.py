import socket


def ipv4_to_hex(ip):
    return socket.inet_aton(ip).hex()