# ex11_21.py
import numpy as np
import matplotlib.pyplot as plt

# 設定 x 和 y 的範圍
x = np.linspace(-2, 2, 200)
y = np.linspace(-2, 2, 200)

# 建立網格
X, Y = np.meshgrid(x, y)

# 計算 Z = log10(1 + x^2 + y^2)
Z = np.log10(1 + X**2 + Y**2)

# 建立畫布與 2 個子圖（左右排列）
fig, ax = plt.subplots(1, 2, figsize=(12, 6), subplot_kw={'projection': '3d'})

# 左邊：三維等高線圖
ax[0].contour3D(X, Y, Z, levels=[0.1, 0.3, 0.5], cmap='jet')
ax[0].set_title('3D Contour of $log_{10}(1+x^2+y^2)$')
ax[0].set_xlabel('X')
ax[0].set_ylabel('Y')
ax[0].set_zlabel('Z')

# 右邊：三維曲面圖
ax[1].plot_surface(X, Y, Z, cmap='jet', alpha=0.7)
ax[1].set_title('3D Surface of $log_{10}(1+x^2+y^2)$')
ax[1].set_xlabel('X')
ax[1].set_ylabel('Y')
ax[1].set_zlabel('Z')

# 顯示圖形
plt.tight_layout()
plt.show()

'''output---------------------------

---------------------------------'''