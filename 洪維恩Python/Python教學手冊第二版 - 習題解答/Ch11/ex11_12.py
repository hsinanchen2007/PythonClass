# ex11_12.py
import numpy as np
import matplotlib.pyplot as plt

# 定義 x 和 r
x = np.linspace(0, 2 * np.pi, 120)
r = np.sin(6 * x)

# 創建極座標圖
plt.figure(figsize=(6, 6))
ax = plt.subplot(111, projection='polar')
ax.plot(x, r, label=r'$r = \sin(6x)$')

# 設定 r 軸刻度範圍
ax.set_rmin(-1)  # 設定 r 軸最小值
ax.set_rmax(1)   # 設定 r 軸最大值
ax.set_rticks([-1, -0.5, 0, 0.5, 1])  # 設定 r 軸刻度

ax.set_title(r'Polar Plot of $r = \sin(6x)$', fontsize=16)  # 加入標題
plt.show()  # 顯示圖形

'''output--------------------

--------------------------'''