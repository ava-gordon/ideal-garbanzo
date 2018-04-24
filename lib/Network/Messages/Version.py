import random
import time
from lib.utils.IPToHex import ipv4ToHex


class Version:
    def __init__(self,
                 addr_recv,
                 addr_from,
                 version=60002,
                 services=1,
                 start_height=0):
        self.version = version
        self.services = services
        self.timestamp = int(time.time())
        self.addr_recv = addr_recv
        self.addr_from = addr_from
        self.nonce = random.getrandbits(64)
        self.user_agent = ''
        self.start_height = start_height

    def to_hex(self):
        return "{}{}{}{}{}{}{}{}".format(self.version.to_bytes(4, byteorder="little").hex(),
                                         self.services.to_bytes(8, byteorder="little").hex(),
                                         self.timestamp.to_bytes(8, byteorder="little").hex(),
                                         self.addr_recv)


# todo: Move NetworkAddress into "Structures" subfolder if/when I create that
class NetworkAddress:
    """
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
            self.ip = NetworkAddress.IPV4_MAP + ipv4ToHex(ip)
        self.port = port

    def to_hex(self):
        if self.time:
            # todo: check that this is the right byteorder for time
            return "{}{}{}{}".format(self.time.to_bytes(4, byteorder="little"),
                                     self.services.to_bytes(8, byteorder="little"),
                                     self.ip,
                                     self.port.to_bytes(2, byteorder="big"))
        else:
            return "{}{}{}".format(self.services.to_bytes(8, byteorder="little"),
                                   self.ip,
                                   self.port.to_bytes(2, byteorder="big"))
