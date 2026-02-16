# ex14_16.py
import numpy as np
import matplotlib.pyplot as plt
from skimage.data import moon
from skimage import exposure

# 讀取 moon 圖像（為灰階）
img = moon()

# (a) 進行直方圖等化處理
equalized = exposure.equalize_hist(img)
equalized_uint8 = (equalized * 255).astype(np.uint8)

# 建立子圖
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# (b) 第一列：原圖與等化後的圖像
axs[0, 0].imshow(img, cmap='gray')
axs[0, 0].set_title("(b) Original Image")
axs[0, 0].axis('off')

axs[0, 1].imshow(equalized_uint8, cmap='gray')
axs[0, 1].set_title("(b) Equalized Image")
axs[0, 1].axis('off')

# (c) 第二列：原圖與等化後圖像的直方圖
axs[1, 0].hist(img.ravel(), bins=256, color='black')
axs[1, 0].set_title("(c) Histogram of Original")

axs[1, 1].hist(equalized_uint8.ravel(), bins=256, color='black')
axs[1, 1].set_title("(c) Histogram of Equalized")

plt.tight_layout()
plt.show()

'''output-----------------------------------

-----------------------------------------'''