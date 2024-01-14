import socket

def serverTCP(stop_event=None, q=None):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 9999
    serversocket.bind((host, port))
    serversocket.listen(5)

    print('TCP thread started!')
    serversocket.settimeout(1)

    while not stop_event.is_set():
        if not q.empty():
            for i in range(50):
                data = q.get()
                data = data.decode('utf-8', errors='ignore')
                if data:
                    print(data)

    print('TCP Thread has closed.')
    stop_event.clear()
    serversocket.close()




