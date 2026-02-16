# ex14_2.py
from skimage import data
import numpy as np
import matplotlib.pyplot as plt

# 讀取 camera 灰階圖像
camera = data.camera()

# (a) 轉換為二值圖像
binary_img = np.where(camera > 128, 255, 0).astype(np.uint8)

# (b) 顯示原圖與二值圖（1×2 子圖）
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(camera, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(binary_img, cmap='gray')
plt.title("Binary Image (>128=255, <=128=0)")
plt.axis('off')

# (c) 統計像素數量
num_gt_128 = np.sum(camera > 128)
num_le_128 = np.sum(camera <= 128)

print("(c) 像素統計結果：")
print(f"像素值 > 128 的數量：{num_gt_128}")
print(f"像素值 <= 128 的數量：{num_le_128}")

plt.tight_layout()
plt.show()

'''output----------------------------
(c) 像素統計結果：
像素值 > 128 的數量：167859
像素值 <= 128 的數量：94285
----------------------------------'''