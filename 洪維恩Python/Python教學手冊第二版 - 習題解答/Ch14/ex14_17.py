# ex14_17.py
import matplotlib.pyplot as plt
from skimage.morphology import disk

# 建立不同半徑的 disk 結構元素
radii = [1, 4, 8, 32]
disks = [disk(r) for r in radii]

# 建立 1x4 子圖顯示
fig, axs = plt.subplots(1, 4, figsize=(12, 3))

for i, (d, r) in enumerate(zip(disks, radii)):
    axs[i].imshow(d, cmap='gray')
    axs[i].set_title(f"disk({r})")
    axs[i].axis('off')

plt.tight_layout()
plt.show()

'''output----------------------------------

----------------------------------------'''