# ex11_1.py
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(12, 8))   # 建立畫布

# (a) f(x) = x^4 + 6x^3 + 7x + 3, -7 ≤ x ≤ 4
x1 = np.linspace(-7, 4, 400)
y1 = x1**4 + 6*x1**3 + 7*x1 + 3
ax1 = fig.add_subplot(3, 1, 1)  # 第 1 個子圖，3列1欄中的第1個
ax1.plot(x1, y1, label='f(x) = x⁴ + 6x³ + 7x + 3', color='blue')
ax1.set_title('(a)')
ax1.grid(True)
ax1.legend()

# (b) f(x) = 6sin(x+3)cos(x), -π ≤ x ≤ 2π
x2 = np.linspace(-np.pi, 2*np.pi, 400)
y2 = 6 * np.sin(x2 + 3) * np.cos(x2)
ax2 = fig.add_subplot(3, 1, 2)  # 第 2 個子圖
ax2.plot(x2, y2, label='f(x) = 6sin(x+3)cos(x)', color='green')
ax2.set_title('(b)')
ax2.grid(True)
ax2.legend()

# (c) f(x) = (x+3)/(x^2+1), -3 ≤ x ≤ 6
x3 = np.linspace(-3, 6, 400)
y3 = (x3 + 3) / (x3**2 + 1)
ax3 = fig.add_subplot(3, 1, 3)  # 第 3 個子圖
ax3.plot(x3, y3, label='f(x) = (x+3)/(x²+1)', color='red')
ax3.set_title('(c)')
ax3.grid(True)
ax3.legend()

# 自動調整子圖間距
plt.tight_layout()
plt.show()

'''output-----

-----------'''