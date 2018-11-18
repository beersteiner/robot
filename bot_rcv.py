import socket

# Global variables
SRV_IP = '127.0.0.1'
SRV_PT = 10000
BUF_SZ = 1024

# Set us up as a server and listen for a connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SRV_IP, SRV_PT))
s.listen(1)
c, cli = s.accept()

# When connected, display client info
print('Connected to IP: '+ cli[0] + ', port: ' + str(cli[1]))


while True:
    data = c.recv(BUF_SZ)
    if not data: break
    data = data.decode()
    print(data)

c.close()
