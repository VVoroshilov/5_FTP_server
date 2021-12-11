import socket

HOST = 'localhost'
PORT = 9107
sock = socket.socket()
sock.connect((HOST, PORT))


while True:
    request = input('>').encode()
    sock.send(request)
    response = sock.recv(1024)
    response = response.decode()
    if response != "Done":
        print(response)

sock.close()