# ex14_20.py
import numpy as np
import matplotlib.pyplot as plt
from skimage.data import astronaut
from skimage.color import rgb2gray
from skimage.util import random_noise
from skimage.filters import median
from skimage.morphology import disk
from skimage import img_as_ubyte

# 讀取並轉成灰階與 uint8 格式
astro = astronaut()
astro_gray = img_as_ubyte(rgb2gray(astro))

# 複製一份作為雜訊處理的基礎
astro2 = astro_gray.copy()
h, w = astro2.shape

# 隨機選取 10000 個像素設為白色（255）
coords_white = np.random.choice(h * w, size=10000, replace=False)
astro2[np.unravel_index(coords_white, (h, w))] = 255

# 隨機選取 10000 個像素設為黑色（0）
coords_black = np.random.choice(h * w, size=10000, replace=False)
astro2[np.unravel_index(coords_black, (h, w))] = 0

# 顯示加入雜訊後的圖像
plt.figure(figsize=(5, 5))
plt.imshow(astro2, cmap='gray')
plt.title("(a) astro2 with Salt & Pepper Noise")
plt.axis('off')
plt.show()

# (b) 使用 median 濾波器搭配不同的 disk 半徑
radii = [1, 2, 3]
filtered_imgs = [median(astro2, disk(r)) for r in radii]

# 顯示濾波後的圖像
fig, axs = plt.subplots(1, 3, figsize=(12, 4))
for i, (img, r) in enumerate(zip(filtered_imgs, radii)):
    axs[i].imshow(img, cmap='gray')
    axs[i].set_title(f"(b) Median Filter (disk={r})")
    axs[i].axis('off')
plt.tight_layout()
plt.show()

'''output-----

-----------'''