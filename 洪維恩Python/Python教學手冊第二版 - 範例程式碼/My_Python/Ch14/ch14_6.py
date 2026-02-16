# ch14_6.py, 有Alpha通道的圖像的觀察
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook  # 載入Matplotlib的範例資料工具
import imageio.v3 as iio
import numpy as np

file_path = cbook.get_sample_data('logo2.png')	# 取得檔案路徑
img = iio.imread(file_path)     # 讀取圖片, 形狀為 (130, 542, 4)

img_rgb = img[:, :, :3] 			# RGB 通道
alpha = img[:, :, 3]  				# Alpha通道
images = [img_rgb, alpha, img] 	# 要顯示的圖像
cmaps = [None, 'gray', None]   	# 使用的色表

fig, axes = plt.subplots(1, 3, figsize=(18, 6)) 
for ax, image, cmap in zip(axes, images, cmaps):
    ax.imshow(image, cmap=cmap)
    ax.axis('off')
plt.tight_layout()
plt.show()