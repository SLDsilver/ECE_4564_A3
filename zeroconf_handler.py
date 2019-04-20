from six.moves import input
from zeroconf import ServiceBrowser, Zeroconf
import socket

class MyListener(object):
    def __init__(self):
        self.server_ip = "0.0.0.0"
        self.server_port = "8081"
    def remove_service(self, zeroconf, type, name):
        print("Service %s removed" % (name,))

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        if info.name == "LED Server._http._tcp.local.":
            print ("New Server Found:\n\tName: ",info.name,
            "\n\tAddress: ",socket.inet_ntoa(info.address),
            "\n\tPort: ",info.port,
            "\n\tAvailable Colors:",info.properties["colors".encode()].decode(),"\n\n")
            self.server_ip = socket.inet_ntoa(info.address)
            self.server_port = str(info.port)

if __name__=="__main__":
    zeroconf = Zeroconf()
    listener = MyListener()
    browser = ServiceBrowser(zeroconf, "_http._tcp.local.", listener)
    try:
        input("Press enter to exit...\n\n")
    finally:
        zeroconf.close()
