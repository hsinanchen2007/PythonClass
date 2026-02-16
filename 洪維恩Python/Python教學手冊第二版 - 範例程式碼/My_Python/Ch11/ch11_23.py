# ch11_23.py, 細部設定散佈圖資料點的呈現方式
import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng(999)
x = rng.random(60)    			# x 軸座標隨機
y = rng.random(60)			# y 軸座標隨機
colors = rng.random(60)  		# 顏色隨機
sizes = 500 * rng.random(60)	# 標記符號大小隨機

fig,ax = plt.subplots()
sc=ax.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap='viridis')
plt.colorbar(sc, ax = ax)     	# 加入色條
plt.show()