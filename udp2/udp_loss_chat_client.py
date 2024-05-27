from socket import *
import time

port = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
server_address = ('localhost', port)

while True:
    msg = input('-> ')
    if msg.lower() == 'quit':
        print('Exiting chat...')
        break
    
    reTx = 0
    while reTx <= 5:
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), server_address)
        sock.settimeout(2)  # 소켓의 timeout 설정. 해당 timeout 내 메시지 수신을 못하면 timeout 예외 발생
        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except timeout:
            reTx += 1
            print('No ack received, retransmitting... (Attempt {})'.format(reTx))
            continue
        else:
            print('Server ack: ', data.decode())
            break

sock.close()
