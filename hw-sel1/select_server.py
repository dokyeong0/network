import socket
import select

HOST = 'localhost'
PORT = 2500

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
server_socket.setblocking(False)

sockets_list = [server_socket]
clients = {}

print("Server is running...")

def broadcast(message, exclude_socket=None):
    for client_socket in clients:
        if client_socket != exclude_socket:
            try:
                client_socket.send(message)
            except Exception as e:
                print(f"Error sending message: {e}")
                client_socket.close()
                sockets_list.remove(client_socket)
                del clients[client_socket]

while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
    
    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            sockets_list.append(client_socket)
            clients[client_socket] = client_address
            print(f"New connection from {client_address}")
        else:
            try:
                message = notified_socket.recv(1024)
                if message:
                    print(f"Received message from {clients[notified_socket]}: {message.decode()}")
                    broadcast(message, exclude_socket=notified_socket)
                else:
                    print(f"Connection closed from {clients[notified_socket]}")
                    sockets_list.remove(notified_socket)
                    del clients[notified_socket]
            except Exception as e:
                print(f"Error handling message from {clients[notified_socket]}: {e}")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]

    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]
