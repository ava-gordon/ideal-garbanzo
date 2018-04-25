import random
import time
from lib.utils.IPToHex import ipv4_to_hex
from lib.utils.VarStr import VarStr


class Version:
    """
    https://en.bitcoin.it/wiki/Protocol_documentation#version
    """
    def __init__(self,
                 addr_recv,
                 addr_from,
                 version=60002,
                 services=1,
                 start_height=0,
                 port=8333):
        self.version = version
        self.services = services
        self.timestamp = int(time.time())
        self.addr_recv = NetworkAddress(self.services, addr_recv, port)
        self.addr_from = NetworkAddress(self.services, addr_from, port)
        self.nonce = random.getrandbits(64).to_bytes(8, byteorder="big").hex()
        self.user_agent = VarStr('')
        self.start_height = start_height.to_bytes(4, byteorder="little").hex()

    def to_hex(self):
        return "{}{}{}{}{}{}{}{}".format(self.version.to_bytes(4, byteorder="little").hex(),
                                         self.services.to_bytes(8, byteorder="little").hex(),
                                         self.timestamp.to_bytes(8, byteorder="little").hex(),
                                         self.addr_recv.to_hex(),
                                         self.addr_from.to_hex(),
                                         self.nonce,
                                         self.user_agent.to_hex(),
                                         self.start_height)


# todo: Move NetworkAddress into "Structures" subfolder if/when I create that
class NetworkAddress:
    """
    https://en.bitcoin.it/wiki/Protocol_documentation#Network_address
    Utility class to generate the hex representation of a network address data structure.
    """
    IPV4_MAP = '00000000000000000000FFFF'

    def __init__(self, services, ip, port, time=None):
        """
        
        :param services: 
        :param ip: 
        :param port: 
        :param time: Either an integer representing the current timestamp, or None
        """
        # remove this and make a method parameter when we add ipv6 support
        ip_version = 4

        self.time = time
        self.services = services
        if ip_version == 4:
            self.ip = NetworkAddress.IPV4_MAP + ipv4_to_hex(ip)
        self.port = port

    def to_hex(self):
        if self.time:
            # todo: check that this is the right byteorder for time
            return "{}{}{}{}".format(self.time.to_bytes(4, byteorder="little").hex(),
                                     self.services.to_bytes(8, byteorder="little").hex(),
                                     self.ip,
                                     self.port.to_bytes(2, byteorder="big").hex())
        else:
            return "{}{}{}".format(self.services.to_bytes(8, byteorder="little").hex(),
                                   self.ip,
                                   self.port.to_bytes(2, byteorder="big").hex())
