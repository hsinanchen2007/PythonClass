# ch14_15.py, 直方圖等化
from skimage import data, exposure, img_as_ubyte
import matplotlib.pyplot as plt
img = data.camera()

# 不同的直方圖等化函數
img_eq = exposure.equalize_hist(img)
img_adapt = exposure.equalize_adapthist(img, clip_limit=0.03)

images = [img, img_as_ubyte(img_eq), img_as_ubyte(img_adapt)]
titles = ['Original', 'Equalized', 'Adaptive Equalized']

fig, ax = plt.subplots(2, 3, figsize=(15, 8))
for img, a, title in zip(images, ax[0], titles):
    a.imshow(img, cmap='gray')		# 繪製等化後的圖
    a.set_title(title)

for img, a in zip(images, ax[1]):
    a.hist(img.ravel(), bins=256, histtype='step')   # 繪製直方圖
    a.set_xlim(0, 255)
plt.show() 