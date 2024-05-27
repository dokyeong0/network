import socket
import threading

def client_handler(client_socket, address):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            # 클라이언트가 보낸 메시지를 모든 클라이언트에게 전송
            for c in clients:
                c.sendall(data)
        except ConnectionResetError:
            break
    client_socket.close()
    clients.remove(client_socket)

HOST = 'localhost'
PORT = 2500

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

clients = []

print("Server is running...")

while True:
    client_socket, address = server_socket.accept()
    clients.append(client_socket)
    threading.Thread(target=client_handler, args=(client_socket, address)).start()
