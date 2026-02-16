# ch11_14.py, 對數座標
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 6, 64)
fig, ax = plt.subplots(1, 2, figsize = (12, 4))
ax[0].plot(x, x**2, x, x**3)
ax[0].set_title('x, log-y')
ax[0].set_yscale('log')    # 設定 y 軸為對數座標

ax[1].plot(x, x**2, x, x**3)
ax[1].set_title('log-x, log-y')  
ax[1].set_xscale('log')    # 設定 x 軸為對數座標
ax[1].set_yscale('log')    # 設定 y 軸為對數座標
plt.show()