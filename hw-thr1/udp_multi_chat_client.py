import socket
import threading

def receive_messages():
    while True:
        try:
            data = client_socket.recv(1024)
            print(data.decode())
        except ConnectionResetError:
            print("Disconnected from server.")
            break

def send_messages():
    while True:
        message = input()
        client_socket.sendall(message.encode())

HOST = 'localhost'
PORT = 2500

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

receive_thread = threading.Thread(target=receive_messages)
send_thread = threading.Thread(target=send_messages)

receive_thread.start()
send_thread.start()
