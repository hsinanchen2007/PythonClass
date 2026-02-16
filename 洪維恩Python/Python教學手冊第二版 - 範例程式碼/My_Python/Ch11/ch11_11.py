# ch11_11.py, 設定網格線與座標軸刻度
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 8, 32)
y = x * np.sin(x)
fig,ax = plt.subplots(1, 2, figsize = (12, 4))
ax[0].plot(x, y)
ax[0].grid()  				# 設定網格線，或 ax[0].grid(True) 
   
ax[1].plot(x, y, 'r')
ax[1].set_yticks([-4, 0, 4, 8])   # 設定座標軸刻度
ax[1].grid(color='b', alpha=0.5, linestyle=':', linewidth=1)
plt.show()