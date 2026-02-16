# ch11_4.py, 利用plt.subplot() 繪製一個2x3的圖形
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 64)
y = np.sin(x) * np.cos(x)**2					# 計算 y 值
fig, ax = plt.subplots(2, 3, figsize=(12, 6)) 	# 建立 2x3 子圖
ax[0,0].plot(x, y) 			    # 第1個子圖
ax[0,1].plot(x, y, 'ro-') 		# 第2個子圖，紅色實線，圓形標記
ax[0,2].plot(x, y, 'xk') 		# 第3個子圖，黑色 x 標記
ax[1,0].plot(x, y, 'g^:') 		# 第4個子圖，綠色虛線，三角形標記
ax[1,1].plot(x, y, '.') 		# 第5個子圖，小圓點標記
ax[1,2].plot(x, y, 'ms') 		# 第6個子圖，洋紅色方形標記
plt.show()					    # 顯示圖形
