# ch14_7.py, JPEG不同品質設定的影響（原圖、品質70和10）
import matplotlib.pyplot as plt
import imageio.v3 as iio
from skimage import data
import numpy as np

img = data.chelsea()  # 讀取原圖（這裡用chelsea貓咪圖）
iio.imwrite('q70.jpg', img, quality = 70)  	# 儲存成不同品質
iio.imwrite('q10.jpg', img, quality = 10)
img_q70 = iio.imread('q70.jpg')   			# 讀回來
img_q10 = iio.imread('q10.jpg')

images = [img, img_q70, img_q10]  			# 要顯示的圖
titles = ['Original Image', 'Quality 70', 'Quality 10']

fig, axes = plt.subplots(1, 3, figsize=(18, 6))
for ax, image, title in zip(axes, images, titles):
    ax.imshow(image)
    ax.set_title(title, fontsize=24)
    ax.axis('off')
plt.tight_layout()
plt.show()