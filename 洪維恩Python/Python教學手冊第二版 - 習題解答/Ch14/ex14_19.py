# ex14_19.py
import matplotlib.pyplot as plt
from skimage.data import moon
from skimage.filters import gaussian, unsharp_mask

# 讀取 moon 圖像（灰階）
img = moon()

# (a) 柔化處理，sigma = 1, 5, 9
sigmas = [1, 5, 9]
smoothed_imgs = [gaussian(img, sigma=s, preserve_range=True).astype('uint8') for s in sigmas]

# 顯示柔化處理結果
fig, axs = plt.subplots(1, 3, figsize=(12, 4))
for i, (s_img, s) in enumerate(zip(smoothed_imgs, sigmas)):
    axs[i].imshow(s_img, cmap='gray')
    axs[i].set_title(f"(a) Gaussian Blur\nsigma={s}")
    axs[i].axis('off')
plt.tight_layout()
plt.show()

# (b) 銳利化處理，amount = 3, 5, 10
amounts = [3, 5, 10]
sharpened_imgs = [unsharp_mask(img, radius=1, amount=a, preserve_range=True).astype('uint8') for a in amounts]

# 顯示銳利化處理結果
fig, axs = plt.subplots(1, 3, figsize=(12, 4))
for i, (sh_img, a) in enumerate(zip(sharpened_imgs, amounts)):
    axs[i].imshow(sh_img, cmap='gray')
    axs[i].set_title(f"(b) Unsharp Mask\namount={a}")
    axs[i].axis('off')
plt.tight_layout()
plt.show()

'''output---------------------------------------

---------------------------------------------'''