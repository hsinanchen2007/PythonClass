# ch11_20.py, 極座標繪圖
import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 2*np.pi, 64)

fig,ax=plt.subplots(subplot_kw={'projection':'polar'}) # 極座標系統
ax.plot(t,np.sqrt(t), 'r', linewidth = 4)
ax.set_rticks([0, 1, 2])
ax.set_rmax(3)
ax.set_rlabel_position(-45)
plt.show()