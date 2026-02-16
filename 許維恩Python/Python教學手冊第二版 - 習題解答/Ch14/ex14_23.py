# ex14_23.py
import matplotlib.pyplot as plt
import numpy as np
from skimage import data
from skimage.draw import disk
from skimage.restoration.inpaint import inpaint_biharmonic

# 讀取chelsea圖像
cat = data.chelsea()

# 建立破損遮罩
np.random.seed(2022)
mask = np.zeros(cat.shape[:2], dtype=bool)
radius = 4  # 圓形區域的半徑
for _ in range(160):
    # 隨機生成圓形的中心點
    x = np.random.randint(radius, cat.shape[0] - radius)
    y = np.random.randint(radius, cat.shape[1] - radius)
    
    # 使用disk函數創建圓形遮罩
    rr, cc = disk((x, y), radius)
    mask[rr, cc] = True

# 生成破損圖像
cat_damage = cat.copy()
cat_damage[mask] = 0  # 將破損區域設為黑色（0）

# 修復破損圖像
cat_restored = inpaint_biharmonic(cat_damage, mask, channel_axis=2)

# 顯示結果
fig, ax = plt.subplots(1, 3, figsize=(15, 5))

# 顯示破損區域
ax[0].imshow(mask, cmap='gray')
ax[0].set_title('Damage Mask')
ax[0].axis('off')

# 顯示破損圖像
ax[1].imshow(cat_damage)
ax[1].set_title('Damaged Image')
ax[1].axis('off')

# 顯示修復後圖像
ax[2].imshow(cat_restored)
ax[2].set_title('Restored Image')
ax[2].axis('off')

fig.tight_layout()
plt.show()

'''output---------------------------

---------------------------------'''