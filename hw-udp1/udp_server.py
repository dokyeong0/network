from socket import *

BUFF_SIZE = 1024
port = 5555
mailboxes = {}

def handle_send(mbox_id, message):
    if mbox_id not in mailboxes:
        mailboxes[mbox_id] = []
    mailboxes[mbox_id].append(message)
    return "OK"

def handle_receive(mbox_id):
    if mbox_id in mailboxes and mailboxes[mbox_id]:
        return mailboxes[mbox_id].pop(0)
    else:
        return "No messages"

s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(('', port))
print('Server is listening...')

while True:
    data, addr = s_sock.recvfrom(BUFF_SIZE)
    message = data.decode().strip()
    print(f"Received: '{message}' from {addr}")

    if message.startswith("send "):
        _, mbox_id, msg = message.split(" ", 2)
        response = handle_send(mbox_id, msg)
    elif message.startswith("receive "):
        _, mbox_id = message.split(" ", 1)
        response = handle_receive(mbox_id)
    elif message == "quit":
        print("Shutting down server.")
        break
    else:
        response = "Invalid command"

    s_sock.sendto(response.encode(), addr)

s_sock.close()
