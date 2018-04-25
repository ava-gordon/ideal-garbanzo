import socket
from lib.Network.Messages.Version import Version
from lib.Network.Messages.Verack import Verack
from lib.Network.Messages.Message import Message

class NetworkHandler:
    """
    A class to manage talking to peers on the bitcoin network. Will find a peer to communicate with,
    and handle sending transactions. 
    """
    DNS_PEER_LIST_MAIN = 'bitseed.xf2.org'
    DNS_PEER_LIST_TEST = ""
    BTC_PORT_MAIN = 8333
    BTC_PORT_TEST = 18333
    VERSION = 60002  # unsure which features came in which versions - let's at least pick a pre-segwit version

    def __init__(self):
        # peer_ip_info = socket.getaddrinfo(NetworkHandler.DNS_PEER_LIST_TEST, 80)
        # self.ip_list = [peer_ip[4][0] for peer_ip in peer_ip_info]
        # self.primary_peer = ''

        # at some point, implement a public IP getter to set this correctly - but it should still work as is
        self.addr_from = '127.0.0.1'

        # print("Finding peers...")
        #
        # #for ip in self.ip_list:
        # ip = self.ip_list[0]
        # print(ip)

        self.ip = "185.28.76.179"  # just use this peer for now - address of testnet faucet

        version = Version(self.ip, self.addr_from)
        print(version.to_hex())

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.ip, NetworkHandler.BTC_PORT_TEST))
            sock.send(Message('version', version.to_hex()).to_bytes())
            peer_version = sock.recv(1000)

        print(peer_version.hex())

    def send_tx(self, tx):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.ip, NetworkHandler.BTC_PORT_TEST))
            sock.send(Message('tx', tx.to_hex()).to_bytes())