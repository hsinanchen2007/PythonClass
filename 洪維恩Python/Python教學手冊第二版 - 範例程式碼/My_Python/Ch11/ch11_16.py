# ch11_16.py, 以科學記號顯示座標軸的刻度
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 6, 64)

fig, ax = plt.subplots(1, 2, figsize = (12, 4))
ax[0].plot(x, np.exp(2*x))
ax[0].set_title('default')

ax[1].plot(x, np.exp(2*x))
ax[1].set_title('scientific')
ax[1].ticklabel_format(axis='y', style='sci', scilimits=(-3,3))
plt.show()