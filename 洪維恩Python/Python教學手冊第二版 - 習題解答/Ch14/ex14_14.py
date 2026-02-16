# ex14_14.py
import matplotlib.pyplot as plt
from skimage.data import camera
from skimage.transform import rotate, rescale, resize

# 讀取 camera 灰階圖像
img = camera()

# (a) 旋轉 30 度，避免裁切，黑色填補
rotated_img = rotate(img, angle=30, resize=True, mode='constant', cval=0)

# (b) 高與寬各放大 2 倍
scaled_img = rescale(img, scale=2.0, anti_aliasing=True)

# (c) 高度改為 480，寬度改為 640
resized_img = resize(img, (480, 640), anti_aliasing=True)

# 顯示三張結果圖
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

axs[0].imshow(rotated_img, cmap='gray')
axs[0].set_title("(a) Rotated 30° (no crop)")
axs[0].axis('off')

axs[1].imshow(scaled_img, cmap='gray')
axs[1].set_title("(b) Scaled 2×")
axs[1].axis('off')

axs[2].imshow(resized_img, cmap='gray')
axs[2].set_title("(c) Resized to 640×480")
axs[2].axis('off')

plt.tight_layout()
plt.show()

'''output----------------------------------------------

----------------------------------------------------'''