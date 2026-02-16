# ch11_28.py, 三維等高線圖與三維曲面圖
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-3, 3, 128)
y = np.linspace(-3, 3, 128)
XX, YY = np.meshgrid(x, y)
ZZ = (1 - XX**3 + YY**3) * np.exp(-XX**2 - YY**2)

fig,ax= plt.subplots(1,2,figsize=(9,4),subplot_kw={'projection':'3d'})
c = ['red','blue','black']
ax[0].contour3D(XX, YY, ZZ, [-.1,.1,.7], linewidths=[2,3,4], colors=c)

ax[1].contour3D(XX, YY, ZZ, [-.1,.1,.7], linewidths=[2,3,4], colors=c)
ax[1].plot_surface(XX, YY, ZZ, cmap='jet', alpha=0.7)
plt.show()