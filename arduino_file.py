import serial

def arduino(stop_event=None, q=None, p=None):
    arduino = serial.Serial('COM3', baudrate=9600, timeout=.1)
    print('Arduino thread is started.')
    for i in range(50):

        if stop_event.is_set():
            arduino.close()
            stop_event.clear()
            print('Arduino thread has closed.')
            break  # Exit the loop if the stop_event is set

        data = arduino.readline()
        '''if data:
            print(i, data)'''
        q.put(data)
        p.put(data)

    if arduino.isOpen():
        arduino.close()
        print('Arduino thread has closed.')
