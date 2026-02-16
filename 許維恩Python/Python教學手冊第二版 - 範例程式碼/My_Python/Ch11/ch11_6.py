# ch11_6.py, 利用 plt.plot() 同時繪製兩個函數的圖形
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2*np.pi, 48)
plt.plot(x, np.sin(x),'r-', x, np.cos(x),'b.')  # 繪製兩個函數圖
plt.xlabel('x-axis')   # x 軸標籤
plt.ylabel('y-axis')   # y 軸標籤
plt.show()