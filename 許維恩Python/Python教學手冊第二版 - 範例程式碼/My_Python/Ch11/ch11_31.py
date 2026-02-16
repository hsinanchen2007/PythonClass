# ch11_31.py, 圓球沿著 y=sin(2x) 的軌跡移動
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter
import matplotlib.pyplot as plt
x = np.linspace(0, 2*np.pi, 100)
y = x * np.sin(2*x)
fig, ax =plt.subplots()

ax.set_xlim(0, 2*np.pi)
ax.set_ylim(min(y)-1, max(y)+1)
ax.plot(x, y)  		# 畫出軌跡線
dot, = ax.plot([], [], 'ro', markersize=12)  # 移動中的紅點

def init():			# 初始化函數
    dot.set_data([], [])
    return dot,
def animate(i):		# 動畫函數
    dot.set_data([x[i]], [y[i]])
    return dot,

ani=FuncAnimation(fig, animate, frames = len(x),
init_func = init, interval = 50)
ani.save("Ch11/ch11_31.gif", writer = PillowWriter(fps = 20))
plt.show()