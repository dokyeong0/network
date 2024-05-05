from socket import *

def send_calculation(sock, calculation):
    sock.send(calculation.encode())

def receive_result(sock):
    return sock.recv(1024).decode()

def main():
    server_address = ('localhost', 3333)
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(server_address)
    
    print("Connected to server.")
    
    while True:
        calculation = input("Enter calculation: ")
        if calculation.lower() == 'q':
            break
        
        send_calculation(client_socket, calculation)
        result = receive_result(client_socket)
        print("Result:", result)
    
    client_socket.close()

if __name__ == "__main__":
    main()
