# ex14_3.py
from skimage import data
import numpy as np
import matplotlib.pyplot as plt

# 讀取原圖（512×512 灰階圖）
camera = data.camera()

# (a) 像素值大於128的分佈圖（白色為True）
mask_a = (camera > 128).astype(np.uint8) * 255

# (b) 像素值介於120~180之間（含120與180）
mask_b = ((camera >= 120) & (camera <= 180)).astype(np.uint8) * 255

# (c) 像素值等於0的分佈圖
mask_c = (camera == 0).astype(np.uint8) * 255

# 繪圖
plt.figure(figsize=(10, 8))

# (a)
plt.subplot(2, 2, 1)
plt.imshow(mask_a, cmap='gray')
plt.title("(a) Pixel > 128")
plt.axis('off')

# (b)
plt.subplot(2, 2, 2)
plt.imshow(mask_b, cmap='gray')
plt.title("(b) 120 ≤ Pixel ≤ 180")
plt.axis('off')

# (c)
plt.subplot(2, 2, 3)
plt.imshow(mask_c, cmap='gray')
plt.title("(c) Pixel == 0")
plt.axis('off')

# 原圖
plt.subplot(2, 2, 4)
plt.imshow(camera, cmap='gray')
plt.title("Original Camera")
plt.axis('off')

plt.tight_layout()
plt.show()

'''output-----

-----------'''