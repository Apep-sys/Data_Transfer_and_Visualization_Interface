import socket
import time
def serverTCP():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 9999
    serversocket.bind((host, port))
    serversocket.listen(5)

    #clientsocket, addr = serversocket.accept()
    print('Thread started!')
    for i in range(0, 5):
        time.sleep(1)
        print('Running')


