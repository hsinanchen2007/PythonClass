# ch11_27.py, 繪製等高線圖
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-3, 3, 128)
y = np.linspace(-3, 3, 128)
XX, YY = np.meshgrid(x, y)
ZZ = (1 - XX**3 + YY**3) * np.exp(-XX**2 - YY**2)

fig, ax = plt.subplots(1, 2, figsize = (12, 4))
cs = ax[0].contour(XX, YY, ZZ, [-0.1, 0, 0.1, 0.3, 0.7, 0.9])
ax[0].clabel(cs, inline=1, fontsize=8)

ax[1].contour(XX, YY, ZZ, 8, colors='black')
ax[1].contourf(XX, YY, ZZ, 8, alpha=.75, cmap='jet')
plt.show()