# ex11_18.py
import numpy as np
import matplotlib.pyplot as plt

# (a) f(x, y) = sin(x) * sin(y)
x = np.linspace(0, 2 * np.pi, 200)
y = np.linspace(0, 2 * np.pi, 200)
XX, YY = np.meshgrid(x, y)
ZZ = np.sin(XX) * np.sin(YY)

# 建立畫布與 4x3 子圖
fig, ax = plt.subplots(4, 3, figsize=(16, 12))

# (a) 2D 等高線圖
ax[0, 0].contour(XX, YY, ZZ, levels=[-0.7, -0.3, 0, 0.3, 0.7], cmap='coolwarm')
ax[0, 0].clabel(ax[0, 0].contour(XX, YY, ZZ, levels=[-0.7, -0.3, 0, 0.3, 0.7], cmap='coolwarm'))
ax[0, 0].set_title('(a) 2D Contour of $f(x,y)=\\sin(x)\\sin(y)$')
# (a) 3D 等高線圖
ax[0, 1] = fig.add_subplot(4, 3, 2, projection='3d')
ax[0, 1].contour3D(XX, YY, ZZ, levels=[-0.7, -0.3, 0, 0.3, 0.7], cmap='coolwarm')
ax[0, 1].set_title('(a) 3D Contour of $f(x,y)=\\sin(x)\\sin(y)$')
# (a) 3D 曲面圖
ax[0, 2] = fig.add_subplot(4, 3, 3, projection='3d')
ax[0, 2].plot_surface(XX, YY, ZZ, cmap='coolwarm', alpha=0.7)
ax[0, 2].set_title('(a) 3D Surface of $f(x,y)=\\sin(x)\\sin(y)$')

# (b) f(x, y) = 1 / sqrt(x² + y² + 1)
x = np.linspace(-np.pi, np.pi, 200)
y = np.linspace(-np.pi, np.pi, 200)
XX, YY = np.meshgrid(x, y)
ZZ = 1 / np.sqrt(XX**2 + YY**2 + 1)
# (b) 2D 等高線圖
ax[1, 0].contour(XX, YY, ZZ, levels=5, cmap='viridis')
ax[1, 0].clabel(ax[1, 0].contour(XX, YY, ZZ, levels=5, cmap='viridis'))
ax[1, 0].set_title('(b) 2D Contour of $f(x,y)=\\frac{1}{\\sqrt{x^2+y^2+1}}$')
# (b) 3D 等高線圖
ax[1, 1] = fig.add_subplot(4, 3, 5, projection='3d')
ax[1, 1].contour3D(XX, YY, ZZ, levels=5, cmap='viridis')
ax[1, 1].set_title('(b) 3D Contour of $f(x,y)=\\frac{1}{\\sqrt{x^2+y^2+1}}$')
# (b) 3D 曲面圖
ax[1, 2] = fig.add_subplot(4, 3, 6, projection='3d')
ax[1, 2].plot_surface(XX, YY, ZZ, cmap='viridis', alpha=0.7)
ax[1, 2].set_title('(b) 3D Surface of $f(x,y)=\\frac{1}{\\sqrt{x^2+y^2+1}}$')

# (c) f(x, y) = y / (x² + y² + 1)^(4/5)
x = np.linspace(-4, 4, 200)
y = np.linspace(-4, 4, 200)
XX, YY = np.meshgrid(x, y)
ZZ = YY / (XX**2 + YY**2 + 1)**(4/5)
# (c) 2D 等高線圖
ax[2, 0].contour(XX, YY, ZZ, levels=6, cmap='RdBu')
ax[2, 0].clabel(ax[2, 0].contour(XX, YY, ZZ, levels=6, cmap='RdBu'))
ax[2, 0].set_title('(c) 2D Contour of $f(x,y)=\\frac{y}{(x^2+y^2+1)^{4/5}}$')
# (c) 3D 等高線圖
ax[2, 1] = fig.add_subplot(4, 3, 8, projection='3d')
ax[2, 1].contour3D(XX, YY, ZZ, levels=6, cmap='RdBu')
ax[2, 1].set_title('(c) 3D Contour of $f(x,y)=\\frac{y}{(x^2+y^2+1)^{4/5}}$')
# (c) 3D 曲面圖
ax[2, 2] = fig.add_subplot(4, 3, 9, projection='3d')
ax[2, 2].plot_surface(XX, YY, ZZ, cmap='RdBu', alpha=0.7)
ax[2, 2].set_title('(c) 3D Surface of $f(x,y)=\\frac{y}{(x^2+y^2+1)^{4/5}}$')

# (d) f(x, y) = (x² + y) * exp(-x² - y²)
x = np.linspace(-3, 3, 200)
y = np.linspace(-3, 3, 200)
XX, YY = np.meshgrid(x, y)
ZZ = (XX**2 + YY) * np.exp(-XX**2 - YY**2)

# (d) 2D 等高線圖
ax[3, 0].contour(XX, YY, ZZ, levels=6, cmap='plasma')
ax[3, 0].clabel(ax[3, 0].contour(XX, YY, ZZ, levels=6, cmap='plasma'))
ax[3, 0].set_title('(d) 2D Contour of $f(x,y)=(x^2+y)e^{-x^2-y^2}$')
# (d) 3D 等高線圖
ax[3, 1] = fig.add_subplot(4, 3, 11, projection='3d')
ax[3, 1].contour3D(XX, YY, ZZ, levels=6, cmap='plasma')
ax[3, 1].set_title('(d) 3D Contour of $f(x,y)=(x^2+y)e^{-x^2-y^2}$')
# (d) 3D 曲面圖
ax[3, 2] = fig.add_subplot(4, 3, 12, projection='3d')
ax[3, 2].plot_surface(XX, YY, ZZ, cmap='plasma', alpha=0.7)
ax[3, 2].set_title('(d) 3D Surface of $f(x,y)=(x^2+y)e^{-x^2-y^2}$')

plt.tight_layout()  # 調整子圖間距
plt.show()          # 顯示圖形

'''output-----------------------------------

-----------------------------------------'''