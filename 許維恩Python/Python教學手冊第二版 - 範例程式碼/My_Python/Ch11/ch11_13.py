# ch11_13.py, 設定繪圖的範圍
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 6, 64)

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].plot(x, x**2, x, x**3)   # 繪出兩條曲線
ax[0].set_title('default')

ax[1].plot(x, x**2,'r-', x,x**3, 'b--', linewidth=3)
ax[1].set_title('custom range')
ax[1].set_ylim([0, 30])  # 設定 y 軸的顯示範圍
fig.suptitle(r'Setting y-limit', fontsize=16)   # 設定畫布標題
plt.show()