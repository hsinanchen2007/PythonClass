# ch11_29.py, 仰角和方位角的設定
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 36)
y = np.linspace(-10, 10, 36)
XX, YY = np.meshgrid(x, y)
ZZ = np.sin((XX**2 + YY**2)**0.5) / (XX**2 + YY**2)**0.5

fig, ax= plt.subplots(1, 2, figsize = (12, 4),
                     subplot_kw = {'projection':'3d'})
p = ax[0].plot_surface(XX, YY, ZZ, cmap='hsv')
ax[0].set_yticks([-10, 0, 10])
ax[0].set_zticks([0, 0.5, 1])
ax[0].set_title(f'elev={ax[0].elev}, azim={ax[0].azim}')
plt.colorbar(p, ax=ax[0], orientation='vertical', pad=0.05)

ax[1].set_axis_off()
ax[1].plot_surface(XX, YY, ZZ, cmap='jet')
ax[1].view_init(60, -40)
ax[1].set_title(f'elev={ax[1].elev}, azim={ax[1].azim}')
plt.show()