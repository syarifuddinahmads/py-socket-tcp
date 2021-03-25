import socket
import _bot


# config socket untuk client (socket,host,port)
ClientMultiSocket = socket.socket()

print('Waiting for connection response')
# try catch socket connection
try:
    # client socket connect dengan konfigurasi host dan port
    ClientMultiSocket.connect((_bot.host, _bot.port))
except socket.error as e:
    # exception ketika koneksi bermasalah atau tidak stabi bahkan error
    print(str(e))

# listen message dari server
res = ClientMultiSocket.recv(1024)
while True:
    # input client untuk mengirim pesan ke server
    Input = input('Hey there: ')
    # client kirim pesan sesuai dengan input
    ClientMultiSocket.send(str.encode(Input))
    # client listen response dari server
    res = ClientMultiSocket.recv(1024)
    # cetak response dari server setelah client meresponse dengan input pesan
    print(res.decode('utf-8'))
# close koneksi dengan server atau client tutup koneksi
ClientMultiSocket.close()