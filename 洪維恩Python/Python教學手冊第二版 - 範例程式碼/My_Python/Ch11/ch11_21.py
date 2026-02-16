# ch11_21.py, 同時繪製極座標圖與直角座標圖
import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(0,2*np.pi,64)
fig=plt.figure(figsize=(10,4))

ax1 = fig.add_subplot(121, projection='polar')   # 極座標系統
ax1.set_title('polar coordinate')
ax1.set_rticks([-0.5, 0, 0.5, 1])
ax1.plot(t, np.sin(t), '-', linewidth = 3)

ax2 = fig.add_subplot(122)    # 直角座標
ax2.plot(t, np.sin(t), 'r')
ax2.set_title('x-y coordinate')
ax2.set_aspect(2)
plt.show()