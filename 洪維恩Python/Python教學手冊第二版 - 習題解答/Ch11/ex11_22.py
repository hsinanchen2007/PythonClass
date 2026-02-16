# ex11_22.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 設定 x 的範圍
x = np.linspace(0,np.pi,240)
y=np.tan(np.sin(2*x)) - np.sin(np.tan(x))
fig, ax = plt.subplots()    # 設定畫布與軸
# 設定軸範圍
ax.set_xlim(0, np.pi)
ax.set_ylim(min(y)-1, max(y)+1)

# 繪製函數曲線
ax.plot(x, y, color='blue')
dot, = ax.plot([], [], 'ro', markersize=10)

def init():     # 初始化紅球的位置
    dot.set_data([], [])
    return dot,

def animate(i): # 更新動畫的函數   
    dot.set_data([x[i]], [y[i]])
    return dot,

# 建立動畫
ani = FuncAnimation(fig, animate, frames=len(x), init_func=init, interval=50, blit=True)
plt.show()  # 顯示動畫

'''output--------------------

--------------------------'''