# ex14_22.py
import matplotlib.pyplot as plt
import numpy as np
from skimage import data
from skimage.restoration.inpaint import inpaint_biharmonic

# 讀取coins圖像
coins = data.coins()

# 建立破損遮罩
np.random.seed(2022)
mask = np.zeros(coins.shape, dtype=bool)
size = 7  # 每個破損區塊的大小
for _ in range(200):
    x = np.random.randint(0, coins.shape[0] - size)
    y = np.random.randint(0, coins.shape[1] - size)
    mask[x:x+size, y:y+size] = True

# 生成破損圖像，將破損區域設為黑色（0）
coins_damage = coins.copy()
coins_damage[mask] = 0  # 破損區域設為黑色

# 修復破損圖像
coins_restored = inpaint_biharmonic(coins_damage, mask, channel_axis=None)

# 顯示結果
fig, ax = plt.subplots(1, 3, figsize=(15, 5))

# 顯示破損遮罩
ax[0].imshow(mask, cmap='gray')
ax[0].set_title('Damage Mask')
ax[0].axis('off')

# 顯示破損圖像
ax[1].imshow(coins_damage, cmap='gray')
ax[1].set_title('Damaged Image')
ax[1].axis('off')

# 顯示修復後的圖像
ax[2].imshow(coins_restored, cmap='gray')
ax[2].set_title('Restored Image')
ax[2].axis('off')

fig.tight_layout()
plt.show()

'''output---------------------------

---------------------------------'''