from socket import *

def calculate_expression(expression):
    try:
        result = eval(expression)
        return round(result, 1) if isinstance(result, float) else result
    except:
        return "Error: Invalid expression"

def main():
    server_address = ('localhost', 3333)
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(1)
    
    print("Server is ready to receive calculations.")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print("Connection from:", client_address)
        
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            
            result = calculate_expression(data)
            client_socket.send(str(result).encode())
        
        client_socket.close()
    
    server_socket.close()

if __name__ == "__main__":
    main()
