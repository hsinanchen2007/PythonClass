# ch11_2.py, 利用 add_subplot() 同時繪製兩個圖形
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 128)	# 建立 0 到 2π 的資料點
fig = plt.figure(figsize=(12, 4))	# 設定畫布的寬和高 
ax1 = fig.add_subplot(1, 2, 1)  	# 建立1×2的子圖，並取得第1個子圖
ax1.plot(x, np.sin(x), 'r') 		# 繪製 sin(x) 紅色線
ax1.set_title('y=sin(x)') 			# 設定子圖標題

ax2=fig.add_subplot(1, 2, 2)  		# 取得畫布fig中，編號2的子圖
ax2.plot(x, np.cos(x), 'b') 		# 繪製 cos(x) 藍色線
ax2.set_title('y=cos(x)') 			# 設定子圖標題
plt.show()