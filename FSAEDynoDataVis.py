import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


path = 'C:\\Users\\DanHamptonWainwright\\Western Michigan University\\RSO, Formula Racing - Formula SAE\\2020\\Testing\\Dyno\\.CSV dump\\dynodata'

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

def animate(i):
    try:
        graph_data = open(path, 'r').read()
        lines = graph_data.split('\n')
        t = []
        rpm = []
        tau = []
        hp = []
        
        for line in lines:
            if len(line) > 10:
                a, b, c, d = line.split(',')
                t.append(float(a))
                rpm.append(float(b))
                tau.append(float(c))
                hp.append(float(d))
        ax1.clear()
        ax1.plot(t, rpm, linewidth = 1)
        ax1.plot(t, tau, linewidth = 1)
        ax1.plot(t, hp, linewidth = 1)
    
    except:
        pass

ani = animation.FuncAnimation(fig, animate)
plt.show()
