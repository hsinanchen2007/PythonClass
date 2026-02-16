# ch11_15.py, 設定刻度和標籤
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 6, 64)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), x, np.cos(x))
ax.set_yticks([-1, 0, 1])     		# 設定 y 軸的刻度
ax.set_xticks([0, 3.14, 6.28])		# 設定 x 軸的刻度
ax.set_xticklabels([0, r'$\pi$', r'2$\pi$'],fontsize = 12)
ax.minorticks_on()      	# 顯示次要刻度
plt.show()