from matplotlib import pyplot as plt

import matplotlib.animation as animation
import serial

def animate(i, dataList, arduino, ax):
    for i in range(50):
        data = arduino.readline()
        data = data.decode('utf-8', errors='ignore')

    # Decode receive Arduino data as a formatted string

    try:
        arduinoData_float = float(data)  # Convert to float
        dataList.append(arduinoData_float)  # Add to the list holding the fixed number of points to animate

    except:  # Pass if data point is bad
        pass

    dataList = dataList[-50:]  # Fix the list size so that the animation plot 'window' is x number of points

    ax.clear()  # Clear last data frame
    ax.plot(dataList)  # Plot new data frame

    ax.set_ylim([0, 5])  # Set Y axis limit of plot
    ax.set_title("Arduino Data")  # Set title of figure
    ax.set_ylabel("Value")  # Set title of y axis


def start_animation():
    arduino = serial.Serial('COM3', baudrate=9600, timeout=0.5)
    dataList = []  # Create empty list variable for later use

    fig = plt.figure()  # Create Matplotlib plots fig is the 'higher level' plot window
    ax = fig.add_subplot(111)  # Add subplot to main fig window


    # Matplotlib Animation Fuction that takes care of real time plot.
    # Note that 'fargs' parameter is where we pass in our dataList and Serial object.
    ani = animation.FuncAnimation(fig, animate, frames=100, fargs=(dataList, arduino, ax), interval=100)
    plt.show()
    arduino.close()