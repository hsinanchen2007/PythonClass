# ch11_10.py, plot()選項的細部設定，並加入座標軸名稱
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 6, 24)
fig, ax = plt.subplots(1, 2, figsize = (12, 4))
ax[0].plot(x, x*np.sin(x), 'mo-')
ax[1].plot(x, x*np.sin(x), color='blue', marker='s',
           linestyle='--', linewidth=3, markersize=10,
           markerfacecolor='yellow', alpha=0.7)
for i in range(2):      # 利用for迴圈設定座標軸名稱
    ax[i].set_xlabel('x-axis')
    ax[i].set_ylabel('y-axis')
plt.show()