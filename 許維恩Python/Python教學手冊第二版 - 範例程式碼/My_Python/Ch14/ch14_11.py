# ch14_11.py, # 彩色圖像的裁切與像素值的設定
import matplotlib.pyplot as plt
from skimage import data

astr0 = data.astronaut()
astr1 = astr0[0:256, 100:360, :]  				# 圖像裁切
astr2 = astr0.copy()
astr2[ 10: 80,  20: 90, :] = [  0, 255, 0]		# 填上綠色
astr2[350:400,  50:200, :] = [255, 255, 0]		# 填上黃色
astr2[200:300, 400:500, :] = [255,   0, 0]		# 填上紅色

images = [astr0, astr1, astr2]  	# 放到串列中
titles = ['Original Image', 'Cropped Image', 'Modified Image']
fig, ax = plt.subplots(1, 3, figsize=(12, 6))
for img, axis, title in zip(images, ax, titles):
    axis.imshow(img)
    axis.set_title(title)
    axis.axis('off')  				# 去掉座標軸
plt.show()