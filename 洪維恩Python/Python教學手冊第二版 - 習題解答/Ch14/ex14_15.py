# ex14_15.py
import matplotlib.pyplot as plt
from skimage.data import astronaut

# 讀取圖像
img = astronaut()

# 分離三個通道
r = img[:, :, 0]
g = img[:, :, 1]
b = img[:, :, 2]

# 繪製 RGB 直方圖
plt.figure(figsize=(8, 4))
plt.hist(r.ravel(), bins=256, color='red', alpha=0.5, label='Red')
plt.hist(g.ravel(), bins=256, color='green', alpha=0.5, label='Green')
plt.hist(b.ravel(), bins=256, color='blue', alpha=0.5, label='Blue')

# 設定 y 軸範圍
plt.ylim(0, 5000)
plt.title("Histogram of RGB Channels")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.show()

'''output----------------------------

----------------------------------'''