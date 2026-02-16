# ch11_32.py, 一起繪出圓球和函數 y="sin"(2x) 的軌跡
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
x = np.linspace(0, 2 * np.pi, 100)
y = x * np.sin(2 * x)
fig, ax = plt.subplots()
ax.set_xlim(-0.3, 6.5)  # 設定 x 軸範圍
ax.set_ylim(-5.8, 5.8)  # 設定 y 軸範圍
dot, = ax.plot([], [], 'ro', markersize=12)  # 注意dot後面有個逗號
line, = ax.plot([], [])   				   # 注意line後面有個逗號
plt.close()

def animate(i):
    dot.set_data([x[i]], [y[i]])
    line.set_data([x[:i]], [y[:i]])

ani = FuncAnimation(fig=fig, func=animate, frames=100, interval=25)
ani.save("Ch11/ch11_32.gif", writer=PillowWriter(fps=20))