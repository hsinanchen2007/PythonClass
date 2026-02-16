# ch11_1.py, 利用add_subplot() 繪製一個圖形
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 32) 	# 建立-2 到 2 的等距數值,共 32 筆
y= x ** 2					# 每個 x 元素平方
fig = plt.figure()			# 建立畫布物件 fig
ax = fig.add_subplot()   		# 加入一個子圖
ax.plot(x, y, 'r') 			# 繪製紅色曲線圖
plt.show()					# 顯示圖形