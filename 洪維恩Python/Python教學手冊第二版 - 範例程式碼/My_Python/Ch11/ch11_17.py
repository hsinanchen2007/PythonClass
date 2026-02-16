# ch11_17.py, 設定座標軸的比例
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-1, 1, 200)
y = np.sqrt(1 - x**2)

fig, ax = plt.subplots(1, 2)
ax[0].plot(x, y, 'b', x, -y, 'b')
ax[0].set_title('aspect: default')

ax[1].plot(x, y, 'b', x, -y, 'b')
ax[1].set_aspect('equal')    # 設定座標軸等比
ax[1].set_title('aspect: equal')
fig.tight_layout()
plt.show()