# ex14_7.py
import numpy as np
import matplotlib.pyplot as plt
from skimage import data

# 自訂色表（8 種顏色，並正規化到 0~1）
colors = np.array([
    [255, 0, 0],       # red
    [0, 0, 0],         # black
    [255, 255, 255],   # white
    [0, 255, 0],       # green
    [128, 128, 128],   # gray
    [0, 0, 255],       # blue
    [0, 255, 255],     # cyan
    [255, 255, 0]      # yellow
]) / 255.0

# 讀入 skimage 提供的 coffee 圖像（RGB）
img = data.coffee() / 255.0  # skimage.data.coffee() 是 uint8，要轉為 float

# 建立空的編碼陣列
h, w, _ = img.shape
index_array = np.zeros((h, w), dtype=int)

# 對每個像素計算與 8 色表的距離，並找出最接近的顏色索引
for i in range(h):
    for j in range(w):
        pixel = img[i, j]
        diffs = np.sum((colors - pixel) ** 2, axis=1)  # 計算顏色差異的平方和
        index_array[i, j] = np.argmin(diffs)  # 找出最小差異的顏色索引

# 使用 RGB 顏色顯示重建圖像
reconstructed_image = np.zeros((h, w, 3), dtype=np.float32)

# 將最相近的顏色應用到重建圖像
for i in range(h):
    for j in range(w):
        reconstructed_image[i, j] = colors[index_array[i, j]]

# 繪圖顯示原圖與重建圖
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# 顯示原圖
axs[0].imshow(img)
axs[0].set_title("Original Coffee Image")
axs[0].axis('off')

# 顯示重建圖
axs[1].imshow(reconstructed_image)
axs[1].set_title("Reconstructed with Custom Colors")
axs[1].axis('off')

plt.tight_layout()
plt.show()

'''output------------------------------------------

------------------------------------------------'''