# ex11_11.py
import numpy as np
import matplotlib.pyplot as plt

# 定義函數 f(x)
def f(x):
    return np.exp(-0.5 * x) * np.cos(3 * x)

# 生成 32 個從 0 到 π 的點
x = np.linspace(0, np.pi, 32)
y = f(x)

# 繪製圖形
plt.plot(x, y, 'r--', label=r'$f(x) = e^{-0.5x} \cos(3x)$')  # 紅色虛線
plt.scatter(x, y, color='yellow', s=8, zorder=5)  # 大小為 8 的黃色圓點

# 加上標題、標籤與網格
plt.title('My plot', fontsize=18)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)

plt.show()  # 顯示圖形

'''output---------------------------

---------------------------------'''