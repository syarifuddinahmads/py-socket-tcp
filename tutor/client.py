import socket

soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.connect((socket.gethostname(),1234))

fullMsg = ''
while True:
    msg = soc.recv(8)
    if len(msg) <= 0:
        break
    fullMsg += msg.decode('utf-8')

print(fullMsg)