from socket import *

BUFF_SIZE = 1024
port = 5555
server_addr = ('localhost', port)

c_sock = socket(AF_INET, SOCK_DGRAM)

while True:
    command = input('Enter command (send [mboxID] message, receive [mboxID], quit): ')
    
   
    if not command.startswith("send ") and not command.startswith("receive ") and command != "quit":
        print("Invalid command. Please enter a command in the format 'send [mboxID] message', 'receive [mboxID]', or 'quit'.")
        continue
    
    c_sock.sendto(command.encode(), server_addr)
    
    if command == "quit":
        break
    
    data, addr = c_sock.recvfrom(BUFF_SIZE)
    print('Server response:', data.decode())

c_sock.close()
