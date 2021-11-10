import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots()
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.2, 1.2)

x, y = [], []
line, = plt.plot([], [], 'bo')
# title = ax.text(0.5,0.85, "", bbox={'facecolor':'w', 'alpha':0.5, 'pad':5},
#                 transform=ax.transAxes, ha="center")

def update(frame):
    x.append(frame)
    y.append(np.sin(frame))
    line.set_data(x, y)
    # title.set_text("%.2f"%frame)
    #ax.title("frame")
    return line #title


ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128))
plt.show()

# ----------------------
        # x = np.arange(0, 100, 1)
        # y = np.sin(x)
        
        # ax = self.fig.add_subplot(111)
        # ax.plot(x, y, label="Earning rate")
        # ax.set_xlabel("x")
        # ax.set_xlabel("y")

        # # ax.set_title("my sin graph")
        # ax.legend()
        # self.canvas.draw()
        #-------------------
        
        # ax.plot(x, y, "#0c0d0d", label="Earning rate")

 
        # print(x)

        # print(y)

        # plt.plot(x, y, "#0c0d0d", label="Earning rate")
        # plt.legend()
        # plt.show()    