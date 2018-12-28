import sys
import socket

BUF_SZ = 1024 # buffer size for socket transmission

class Xbee:
    def __init__(self, ip, pt):
        self.ip = ip        # xbee ip address
        self.pt = pt        # xbee port number
        self.sk = None      # will hold socket object
    def connect(self):      # use this to establish connection with xbee
        self.sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sk.connect((self.ip, self.pt))
    def send(self, d):      # eg. xbeeA.send('foo')
        if type(d) == str:
            d = d.encode()
        self.sk.send(d)
    def recv(self):         # eg. data = xbeeA.recv()
        self.sk.recv(BUF_SZ)
    def close(self):        # good practice to close socket, although
                            # termination of program will result in closure
        self.sk.close()

