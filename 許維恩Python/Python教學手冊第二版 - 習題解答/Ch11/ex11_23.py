# ex11_23.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 角度參數
t = np.linspace(0, 2*np.pi, 256)
r = np.sin(6 * t)

fig, ax=plt.subplots(subplot_kw={'projection':'polar'})     # 極座標圖
ax.set_ylim(-1, 1.05)
ax.set_yticks([-1.0, -0.5, 0.0, 0.5, 1.0]) # 設定刻度位置

# 初始化紅球和動態線條
dot, = ax.plot([], [], 'ro', markersize=10)    # 紅球
line, = ax.plot([], [], 'b')                   # 曲線

# 初始化函式
def init():
    dot.set_data([], [])
    line.set_data([], [])
    return dot, line

# 更新函式
def update(i):
    dot.set_data([t[i]], [r[i]])           # 更新紅球位置
    line.set_data(t[:i+1], r[:i+1])        # 畫出目前為止的曲線
    return dot, line

# 建立動畫
ani = FuncAnimation(fig, update, frames=len(t), init_func=init, interval=50, blit=True)

plt.title(r"Red Ball Tracing $r = \sin(6t)$")
plt.show()

'''output----------

----------------'''