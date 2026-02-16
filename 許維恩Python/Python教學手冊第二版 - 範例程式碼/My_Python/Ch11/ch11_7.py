# ch11_7.py, 利用 plt.savefig() 儲存繪製的圖形
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 6*np.pi, 120)
y = np.sin(x) * np.exp(-0.2 * x)

fig = plt.figure(figsize = (7, 5))
ax = fig.add_subplot()
ax.plot(x, y, linewidth = 3)	# 指定線條寬度為3個點
ax.grid()     				# 加上網格線
plt.savefig("Ch11\\ch11_7.png", dpi=300, transparent=True)
plt.show()    			# 注意這行要放在plt.savefig()的後面