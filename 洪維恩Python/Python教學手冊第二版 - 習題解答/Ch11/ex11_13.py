# ex11_13.py
import numpy as np
import matplotlib.pyplot as plt

# 定義 x 和兩個 r
x = np.linspace(0, 2 * np.pi, 120)
r1 = np.sin(3 * x)
r2 = np.cos(np.sin(6 * x))

# 創建極座標圖
plt.figure(figsize=(6, 6))
ax = plt.subplot(111, projection='polar')

# 繪製兩條曲線
ax.plot(x, r1, label=r'$r = \sin(3x)$', color='blue')
ax.plot(x, r2, label=r'$r = \cos(\sin(6x))$', color='red')

# 設定 r 軸刻度範圍
ax.set_rmin(-1)  # 設定 r 軸最小值
ax.set_rmax(1)   # 設定 r 軸最大值
ax.set_rticks([-1, 0, 1])  # 設定 r 軸刻度

# 加入標題與圖例
ax.set_title(r'Polar Plot of $r = \sin(3x)$ and $r = \cos(\sin(6x))$', fontsize=16)
ax.legend(loc='lower right', bbox_to_anchor=(1.3, 0))
plt.show()  # 顯示圖形

'''output----------

----------------'''