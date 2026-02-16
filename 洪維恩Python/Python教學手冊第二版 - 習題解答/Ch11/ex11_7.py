# ex11_7.py
import numpy as np
import matplotlib.pyplot as plt

# 建立 x 值（對數範圍）
x = np.logspace(0, 3, 400)  # 相當於從 10^0=1 到 10^3=1000
# 計算 y 值
y = x * np.log10(3 * x) * np.sin(np.sqrt(x))

# 建立圖形
plt.figure(figsize=(8, 5))
plt.plot(x, y, color='darkorange', label=r'$y = x \log_{10}(3x) \sin(\sqrt{x})$')

plt.xscale('log')# 設定 x 軸為對數座標

# 加上標題與標籤
plt.title('y = x log₁₀(3x) sin(√x)')
plt.xlabel('x (log scale)')
plt.ylabel('y')
plt.grid(True, which='both')  # 顯示主次網格
plt.legend()

plt.show()  # 顯示圖形

'''output-----

-----------'''