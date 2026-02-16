# ex14_12.py
import numpy as np
import matplotlib.pyplot as plt
from skimage.data import camera

# 讀取 camera 圖像
img = camera()

# 條件判斷
low_mask = img < 5        # 小於 5
high_mask = img > 250     # 大於 250

# 統計像素數量
low_count = np.sum(low_mask)
high_count = np.sum(high_mask)

print(f"Number of pixels < 5: {low_count}")
print(f"Number of pixels > 250: {high_count}")

# 建立彩色圖像 (RGB)
color_img = np.ones((img.shape[0], img.shape[1], 3))  # 初始化為白色 (1,1,1)

# 將小於 5 的像素設為紅色 (1, 0, 0)
color_img[low_mask] = [1, 0, 0]

# 將大於 250 的像素設為藍色 (0, 0, 1)
color_img[high_mask] = [0, 0, 1]

# 顯示彩色分佈圖
plt.imshow(color_img)
plt.title("Pixels < 5 (Red) and > 250 (Blue)")
plt.axis('off')
plt.show()

'''output--------------------

--------------------------'''