# ex14_18.py
import matplotlib.pyplot as plt
from skimage.data import chelsea
from skimage.color import rgb2gray
from skimage.filters import sobel, gaussian

# 讀取並轉為灰階
img = rgb2gray(chelsea())

# 設定不同的 sigma 值
sigmas = [1, 2, 4]
edges = [sobel(gaussian(img, sigma=s)) for s in sigmas]

# 建立 1×3 子圖
fig, axs = plt.subplots(1, 3, figsize=(12, 4))

for i, (e, s) in enumerate(zip(edges, sigmas)):
    axs[i].imshow(e, cmap='gray')
    axs[i].set_title(f"Sobel + Gaussian (sigma={s})")
    axs[i].axis('off')

plt.tight_layout()
plt.show()

'''output-----------------------------------

-----------------------------------------'''