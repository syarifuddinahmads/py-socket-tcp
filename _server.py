import socket
from _thread import * # import thread
import _bot # import bot library

# config socket untuk server (socket,host,port)
ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 1234

# hitung thread yang berjalan setiap ada koneksi atau client baru
ThreadCount = 0

# try catch binding connection (host,port)
try:
    # bind host & port dari server
    ServerSideSocket.bind((host, port))
except socket.error as e:
    # exception ketika proses binding host & port gagal
    print(str(e))

# listen socket connection
print('Socket is listening..')
ServerSideSocket.listen(5)

# thread untuk handle multiple client secara bersamaan
def multi_threaded_client(connection):
    # kirim pesan sambutan yang telah disediakan di bot library
    connection.send(str.encode(_bot.greetings('')))
    # loop
    while True:
        # receive data from client
        data = connection.recv(2048)
        # bind response dari server berdasar apa yang dikirim client
        response = 'Server message: ' + data.decode('utf-8')
        if not data:
            break
        # kirim data response ke semua client yang terkoneksi berdasarkan response yang telah disediakan di bot library
        connection.sendall(str.encode(_bot.response(response)))
    # tutup koneksi
    connection.close()

# loop listenen
while True:
    # client & address accept connection
    Client, address = ServerSideSocket.accept()
    # cetak info koneksi yang terhubung atau informasi socket yang terhubung
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    # proses thread untuk handle multiple client yng terkoneksi
    start_new_thread(multi_threaded_client, (Client, ))
    # counter thread yang berjalan
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
# tutup koneksi server
ServerSideSocket.close()