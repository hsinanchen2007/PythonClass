# ch14_19.py, 圖像修復的範例
import matplotlib.pyplot as plt
import numpy as np
from skimage import data
from skimage.restoration.inpaint import inpaint_biharmonic

cat = data.chelsea()    # 讀取範例圖像
# 建立破損遮罩
np.random.seed(2022)
mask = np.zeros(cat.shape[:2], dtype=bool)
size = 12  # 每個破損區塊大小
for _ in range(160):
    x = np.random.randint(0, cat.shape[0] - size)
    y = np.random.randint(0, cat.shape[1] - size)
    mask[x:x+size, y:y+size] = True

# 生成破損圖像
cat_damage = cat * ~mask[:, :, np.newaxis]

# 修復破損圖像
out = inpaint_biharmonic(cat_damage, mask, channel_axis=2)

# 顯示結果
fig, ax = plt.subplots(1, 3, figsize=(12, 5))
ax[0].imshow(mask, cmap='gray')
ax[0].set_title('Damage Mask')
ax[0].axis('off')

ax[1].imshow(cat_damage)
ax[1].set_title('Damaged Image')
ax[1].axis('off')

ax[2].imshow(out)
ax[2].set_title('Restored Image')
ax[2].axis('off')

fig.tight_layout()
plt.show()