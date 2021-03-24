import socket
import threading

socClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socClient.connect((socket.gethostname(),1234))

while True:
    try:
        msgFromServer = socClient.recv(1024).decode('utf-8')
        print('Server : ', msgFromServer)
        if msgFromServer == '':
            msgClientInput = input('Tulis Pesan : ')
            socClient.send(bytes(msgClientInput, 'utf-8'))
        else:
            print('Server : ', msgFromServer)
    except:
        print('Error Server !')
        break