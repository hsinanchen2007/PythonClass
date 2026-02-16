# ex11_20.py
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 建立 x 和 y 的網格
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

# 定義 z 函數
Z = (X + Y) * np.exp(-X**2 - Y**2)

# 建立畫布與三維座標軸
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 繪製曲面圖
surf = ax.plot_surface(X, Y, Z, cmap='viridis')

# 設定仰角與方位角
ax.view_init(elev=40, azim=160)

# 加上標題與軸標籤
ax.set_title(r'$z = (x + y) \cdot e^{-x^2 - y^2}$')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()  # 顯示圖形

'''output---------------------

---------------------------'''