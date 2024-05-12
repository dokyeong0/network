from socket import *

mimeType = {
    'html': 'text/html',
    'png': 'image/png',
    'ico': 'image/x-icon'
}

def handle_request(request):
    
    filename = request.split()[1][1:]  

    try:
        
        if filename == '':
            filename = 'index.html'  

        f = open(filename, 'rb')
        file_data = f.read()
        f.close()

        
        file_extension = filename.split('.')[-1]
        if file_extension in mimeType:
            content_type = mimeType[file_extension]
        else:
            content_type = 'application/octet-stream'  

        
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type: {}\r\n\r\n".format(content_type)
        response = response.encode() + file_data

    except FileNotFoundError:
        
        response = "HTTP/1.1 404 Not Found\r\n\r\n"
        response += "<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>"
        response += "<BODY>Not Found</BODY></HTML>"
        response = response.encode()

    return response


server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', 80))
server_socket.listen(5)

print("Web server is running...")

while True:
    client_socket, addr = server_socket.accept()
    request = client_socket.recv(1024).decode()
    if request:
        response = handle_request(request)
        client_socket.send(response)
        client_socket.close()
