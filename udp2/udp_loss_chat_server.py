from socket import *

port = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))
print('Server is running...')

while True:
    data, addr = sock.recvfrom(BUFF_SIZE)
    sock.sendto(b'ack', addr)
    print('<-', data.decode())
