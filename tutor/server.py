import socket

soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.bind((socket.gethostname(),1234))
soc.listen(5)

while True:
    clientSoc, addr = soc.accept()
    print(f"Connection from {addr} has been estabilized !")
    clientSoc.send(bytes('Hello client !','utf-8'))
    clientSoc.close()