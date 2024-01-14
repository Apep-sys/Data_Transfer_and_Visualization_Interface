import socket
import time
def serverTCP(stop_event=None, q=None):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 9999
    serversocket.bind((host, port))
    serversocket.listen(5)

    if not q.empty():
        print('TCP thread started!')
        for i in range(50):

            if stop_event.is_set():
                print('TCP Thread has closed.')
                serversocket.close()

            data = q.get()
            data = data.decode('utf-8', errors='ignore')
            if data:
                print(data)
    else:
        print('Can not start TCP thread because queue is empty.')



