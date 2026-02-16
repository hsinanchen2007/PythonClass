# ex14_1.py
import numpy as np
from skimage import data
import matplotlib.pyplot as plt

# 載入圖像
camera = data.camera()
coins = data.coins()
astronaut = data.astronaut()

images = {
    'camera': camera,
    'coins': coins,
    'astronaut': astronaut
}

# (a) 顯示每張圖的 shape 與 dtype
print("(a) 每張圖像的 shape 和 dtype：")
for name, img in images.items():
    print(f"{name}: shape = {img.shape}, dtype = {img.dtype}")

# (b) 判斷灰階或彩色
print("\n(b) 圖像型態判斷（灰階 / 彩色）：")
for name, img in images.items():
    if img.ndim == 2:
        print(f"{name}: 灰階圖像")
    elif img.ndim == 3 and img.shape[2] == 3:
        print(f"{name}: 彩色圖像")
    else:
        print(f"{name}: 無法判斷")

# 繪圖：上排原圖，下排紅色標記圖
print("\n(c) 繪製像素值等於0的分佈圖（上排原圖，下排標記圖）")
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 8))

for idx, (name, img) in enumerate(images.items()):
    # 上排第 idx 欄 - 原圖
    ax_orig = axes[0, idx]
    if img.ndim == 3:
        ax_orig.imshow(img)
    else:
        ax_orig.imshow(img, cmap='gray')
    ax_orig.set_title(f"{name} - Original")
    ax_orig.axis('off')

    # 先轉灰階處理
    if img.ndim == 3:
        gray = np.mean(img, axis=2).astype(np.uint8)
    else:
        gray = img

    gray_rgb = np.stack([gray]*3, axis=2)
    red_mask = (gray == 0)
    gray_rgb[red_mask] = [255, 0, 0]

    # 下排第 idx 欄 - 像素值為0紅色標記
    ax_zero = axes[1, idx]
    ax_zero.imshow(gray_rgb)
    ax_zero.set_title(f"{name} - pixel=0(red mark)")
    ax_zero.axis('off')

plt.tight_layout()
plt.show()

'''output------------------------------------
(a) 每張圖像的 shape 和 dtype：
camera: shape = (512, 512), dtype = uint8
coins: shape = (303, 384), dtype = uint8
astronaut: shape = (512, 512, 3), dtype = uint8

(b) 圖像型態判斷（灰階 / 彩色）：
camera: 灰階圖像
coins: 灰階圖像
astronaut: 彩色圖像

(c) 繪製像素值等於0的分佈圖
------------------------------------------'''