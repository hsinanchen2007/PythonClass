# ch14_18.py, 利用median() 函數進行去除雜訊
import matplotlib.pyplot as plt
import numpy as np
from skimage import data
from skimage.filters.rank import median		# 載入median()
from skimage.morphology import disk		# 載入disk()

man = data.camera() 						# 讀取範例圖像
noise = np.random.rand(*man.shape) 			# 加入椒鹽雜訊
man[noise > 0.98] = 255
man[noise < 0.02] = 0
fig, ax = plt.subplots(1, 3, figsize=(10, 4))	# 建立子圖

ax[0].imshow(man, cmap='gray')   # 顯示帶有雜訊的原圖
ax[0].set_title('Noisy Image')
ax[0].axis('off')

ax[1].imshow(median(man, disk(1)), cmap='gray')  # 使用小範圍濾波
ax[1].set_title('Median Filter (disk=1)')
ax[1].axis('off')

ax[2].imshow(median(man, disk(10)), cmap='gray') # 使用大範圍濾波
ax[2].set_title('Median Filter (disk=10)')
ax[2].axis('off')

fig.tight_layout()
plt.show()