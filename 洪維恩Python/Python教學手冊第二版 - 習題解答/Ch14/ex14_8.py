# ex14_8.py
import numpy as np
import matplotlib.pyplot as plt
from skimage import data
from matplotlib.colors import ListedColormap

# 建立灰階色表，灰階值範圍從 0 到 1（11 個顏色）
gray_values = np.linspace(0, 1, 11)
gray_colors = np.array([[x, x, x] for x in gray_values])  # RGB 為相同的 x 值

# 建立自訂灰階色表
cmap = ListedColormap(gray_colors)

# 讀取 camera 圖像，並轉換為浮點數型態
img = data.camera() / 255.0  # 轉換為浮點數（0~1 範圍）

# 建立空的量化結果陣列
h, w = img.shape
quantized_image = np.zeros((h, w), dtype=int)

# 將每個像素映射到最接近的灰階值
for i in range(h):
    for j in range(w):
        pixel_value = img[i, j]
        diffs = (gray_values - pixel_value) ** 2  # 計算每個灰階色與像素的差異
        quantized_image[i, j] = np.argmin(diffs)  # 找出最小差異的索引

# 顯示原始圖像與量化後的圖像
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

axs[0].imshow(img, cmap="gray")
axs[0].set_title("Original Camera Image")
axs[0].axis('off')

axs[1].imshow(quantized_image, cmap=cmap)
axs[1].set_title("Quantized Image with 11 Grayscale Levels")
axs[1].axis('off')

plt.tight_layout()
plt.show()

'''output-----

-----------'''