import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from multiprocessing import Process
import serial
import pandas as pd
import numpy as np

port  = 'COM6'
path = 'C:\\Users\\DanHamptonWainwright\\Western Michigan University\\RSO, Formula Racing - Formula SAE\\2020\\Testing\\Dyno\\.CSV dump\\dynodata'


ser = serial.Serial(port, 921600)

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

def animate(i):
    graph_data = open(path, 'r').read()
    lines = graph_data.split('\n')
    x = []
    y1 = []
    y2 = []

    for line in lines:
        if len(line) > 1:
            a, b, c = line.split(',')
            x.append(float(a))
            y1.append(float(b))
            y2.append(float(c))
    ax1.clear()
    ax1.plot(x, y1)
    ax1.plot(x, y2)

def getserial():
    packet = ser.readline()
    df = pd.DataFrame(packet)
    df.to_csv(path)

if __name__ == '__main__':
    DAQ = Process(target = getserial)
    DAQ.start()

ani = animation.FuncAnimation(fig, animate, interval=250)
plt.show()
