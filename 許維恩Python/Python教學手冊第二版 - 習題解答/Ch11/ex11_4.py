# ex11_4.py
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2 * np.pi, 400)              # 建立 x 範圍
fig, axes = plt.subplots(2, 2, figsize=(10, 6)) # 建立圖與 2x2 子圖區

# f1(x) = sin(x)
axes[0, 0].plot(x, np.sin(x), color='blue')
axes[0, 0].set_title(r'$f_1(x) = \sin(x)$')
axes[0, 0].grid(True)

# f2(x) = sin(2x)
axes[0, 1].plot(x, np.sin(2*x), color='green')
axes[0, 1].set_title(r'$f_2(x) = \sin(2x)$')
axes[0, 1].grid(True)

# f3(x) = sin(3x)
axes[1, 0].plot(x, np.sin(3*x), color='red')
axes[1, 0].set_title(r'$f_3(x) = \sin(3x)$')
axes[1, 0].grid(True)

# f4(x) = sin(4x)
axes[1, 1].plot(x, np.sin(4*x), color='purple')
axes[1, 1].set_title(r'$f_4(x) = \sin(4x)$')
axes[1, 1].grid(True)

# 自動調整間距避免標題重疊
plt.tight_layout()
plt.show()

'''output------

------------'''