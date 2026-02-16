# ch11_5.py, 利用 plt.plot() 繪製一個3次多項式的圖形
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 5, 32)   	# 建立從 -2 到 5 的資料點
y = x**3 - 4 * x**2 + 6      	# 計算 3 次多項式
plt.plot(x, y)               	# 直接以plt.plot()繪圖
plt.title('Cubic poly')     	# 加上圖形的標題
plt.show()