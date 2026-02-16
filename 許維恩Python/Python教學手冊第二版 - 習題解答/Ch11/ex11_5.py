# ex11_5.py
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2 * np.pi, 400)# 建立 x 值
# 計算三個函數
y1 = np.sin(x)
y2 = np.cos(2 * x)
y3 = y1 + y2
# 建立畫布與 3x1 子圖
fig, axes = plt.subplots(3, 1, figsize=(5, 10))

# f1(x) = sin(x)
axes[0].plot(x, y1, color='red')
axes[0].set_title(r'$f_1(x) = \sin(x)$')
axes[0].grid(True)

# f2(x) = cos(2x)
axes[1].plot(x, y2, color='green')
axes[1].set_title(r'$f_2(x) = \cos(2x)$')
axes[1].grid(True)

# f3(x) = sin(x) + cos(2x)
axes[2].plot(x, y3, color='blue')
axes[2].set_title(r'$f_3(x) = \sin(x) + \cos(2x)$')
axes[2].grid(True)

# 自動調整間距避免重疊
plt.tight_layout()
plt.show()

'''output-----

-----------'''