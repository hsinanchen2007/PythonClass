# ch11_30.py, 三維的散佈圖
import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(1, 15, 120)
x = np.cos(t) / np.sqrt(t)
y = np.sin(t) / np.sqrt(t)

fig,ax= plt.subplots(1, 2, figsize=(10,4), subplot_kw={'projection':'3d'})
p = ax[0].scatter(x, y, t, c=t, cmap='jet')
plt.colorbar(p, ax=ax[0], orientation='vertical', fraction=0.035, pad=0.05)

ax[1].plot(x, y, t,'-')
ax[1].grid(False)
plt.show()