import socket
import threading
import sys

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024)
            if message:
                print(message.decode())
            else:
                print("Disconnected from server")
                sock.close()
                return
        except Exception as e:
            print(f"Error receiving message: {e}")
            sock.close()
            return

def send_messages(sock):
    while True:
        message = input()
        if message.lower() == 'quit':
            sock.send(message.encode())
            sock.close()
            sys.exit()
        else:
            try:
                sock.send(message.encode())
            except Exception as e:
                print(f"Error sending message: {e}")
                sock.close()
                return

HOST = 'localhost'
PORT = 2500

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
send_thread = threading.Thread(target=send_messages, args=(client_socket,))

receive_thread.start()
send_thread.start()
