#program untuk server9
import socket


listenerSocket = socket.socket()
serverIP = "0.0.0.0"
serverPort = 2222

listenerSocket.bind((serverIP,serverPort))
listenerSocket.listen(0)
print("server menunggu koneksi dari client")

while True:
    handler, addr = listenerSocket.accept()
    print("sebuah client terkoneksi dengan alamat:{}".format(addr))
while True:
    message = input("masukan pesan anda : ")
    handler.send(message.encode())
    message = handler.recv(1024)
    print("pesan dari client : {}".format(message.decode("utf-8")))





