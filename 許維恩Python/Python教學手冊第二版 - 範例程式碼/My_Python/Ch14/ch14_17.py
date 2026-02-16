# ch14_17.py, 柔化與銳利化圖像
import matplotlib.pyplot as plt
from skimage import data
from skimage.filters import unsharp_mask, gaussian	 # 載入套件

cat = data.chelsea()
fig, ax = plt.subplots(1, 3, figsize=(10, 4))		 # 建立子圖

ax[0].imshow(gaussian(cat, sigma=3, channel_axis=2))	 # 柔化
ax[0].set_title('Gaussian Blur')
ax[0].axis('off')

ax[1].imshow(cat)    # 顯示原圖
ax[1].set_title('Original')
ax[1].axis('off')

ax[2].imshow(unsharp_mask(cat, amount=5, channel_axis=2))  # 銳利化
ax[2].set_title('Unsharp Mask')
ax[2].axis('off')
fig.tight_layout()
plt.show()