# ch14_13.py, # 色彩空間轉換的範例
import matplotlib.pyplot as plt
from skimage import data
from skimage.color import rgb2gray, rgb2hsv

img = data.astronaut()	
gray_img = rgb2gray(img)			# 轉換成灰階
hsv_img = rgb2hsv(img)			# 轉換成 HSV
h_channel = hsv_img[:, :, 0]  		# 色相（Hue）
s_channel = hsv_img[:, :, 1]  		# 飽和度（Saturation）

images = [gray_img, h_channel, s_channel]
titles = ['Grayscale', 'Hue Channel', 'Saturation Channel']
fig, ax = plt.subplots(1, 3, figsize=(12, 3))
for img, axis, title in zip(images, ax, titles):
    im = axis.imshow(img, cmap='gray')
    axis.set_title(title)
    axis.axis('off')
    fig.colorbar(im, ax=axis)  		# 加上 colorbar
plt.show()