# ex11_17.py
import numpy as np
import matplotlib.pyplot as plt

# 產生常態分佈資料
mean = 170
std_dev = 16
size = 1200

x = np.random.normal(mean, std_dev, size)
y = np.random.normal(mean, std_dev, size)

# 建立畫布與兩個子圖（左右排列）
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# 使用 plot() 繪製資料點
axes[0].plot(x, y, 'o', markersize=3, alpha=0.5)
axes[0].set_title('Using plot()')
axes[0].set_aspect('equal')  # 設定座標軸比例為 1:1

# 使用 scatter() 繪製資料點
axes[1].scatter(x, y, s=10, alpha=0.5)
axes[1].set_title('Using scatter()')
axes[1].set_aspect('equal')  # 設定座標軸比例為 1:1

# 統一座標軸範圍（可有可無，看是否想比較清楚）
for ax in axes:
    ax.set_xlim(min(x), max(x))
    ax.set_ylim(min(y), max(y))

plt.tight_layout()
plt.show()

'''output----------------------------------

----------------------------------------'''