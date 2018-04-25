import socket
from lib.Network.Messages.Version import Version
from lib.Network.Messages.Verack import Verack

class NetworkHandler:
    """
    A class to manage talking to peers on the bitcoin network. Will find a peer to communicate with,
    and handle sending transactions. 
    """
    DNS_PEER_LIST = 'bitseed.xf2.org'
    BTC_PORT = 8333
    VERSION = 60002  # unsure which features came in which versions - let's at least pick a pre-segwit version

    def __init__(self):
        peer_ip_info = socket.getaddrinfo(NetworkHandler.DNS_PEER_LIST)
        self.ip_list = [peer_ip[4][0] for peer_ip in peer_ip_info]
        self.primary_peer = ''
        print("Finding peers...")

        for ip in self.ip_list:
            vers = Version(ip, )
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, NetworkHandler.BTC_PORT))
            sock.send()
