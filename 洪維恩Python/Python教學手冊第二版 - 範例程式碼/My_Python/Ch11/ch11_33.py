# ch11_33.py, 三維的動畫
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
x = np.linspace(-6, 6, 128)
y = np.linspace(-6, 6, 128)
XX, YY = np.meshgrid(x, y)
ZZ = np.sin(np.sqrt(XX**2 + YY**2))

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot_surface(XX, YY, ZZ, cmap='jet', alpha=0.7)
ax.set_axis_off()
plt.close()

def animate(i):
    ax.view_init(30, i)

ani = FuncAnimation(fig=fig, func=animate, 
frames=np.arange(0, 360, 3), interval=60)
ani.save("Ch11/ch11_33.gif", writer=PillowWriter(fps=20))