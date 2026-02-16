# ex11_9.py
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(1, 100, 400)# 建立 x 值
y = (x * np.exp(x)) / (x**2 + 1)# 計算 y 值

# 建立圖形
plt.figure(figsize=(8, 5))
plt.plot(x, y, color='purple', label=r'$\frac{x e^x}{x^2 + 1}$')

# 設定 x 軸與 y 軸為對數座標
plt.xscale('log')
plt.yscale('log')

# 加上標題與標籤
plt.title(r'$y = \frac{x e^x}{x^2 + 1}$')
plt.xlabel('x (log scale)')
plt.ylabel('y (log scale)')
plt.grid(True, which='both')  # 顯示主次網格線
plt.legend()

plt.show()  # 顯示圖形

'''output-----

-----------'''