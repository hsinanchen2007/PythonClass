# ch11_3.py, 用subplots() 繪製 y=sin(x)cos(2x) 的圖形
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 128) 			# 建立0到2π的資料點
fig, ax = plt.subplots()    				# 同時建立畫布和子圖
ax.plot(x, np.sin(x)*np.cos(2*x), 'r') 		# 繪製圖形，紅色線
plt.show()								    # 顯示圖形