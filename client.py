import socket

connectionSocket = socket.socket()
serverIP = "127.0.0.1"
serverPort = 2222

connectionSocket.connect((serverIP,serverPort))
print("terhubung dengan server")

while True:
    message = connectionSocket.recv(1024)
    print("pesan dari server : {}".format(message.decode("utf-8")))
    message = input("masukan pesan anda")
    connectionSocket.send(message.encode())