# ch14_5.py, 彩色圖像與RGB通道展示
from skimage import data
import matplotlib.pyplot as plt

img = data.astronaut()  # 讀取彩色圖像

# 定義要顯示的資料、標題和子圖
images = [img, img[:, :, 0], img[:, :, 1]]
titles = ['Original Image', 'Red Channel', 'Green Channel']
cmaps = [None, 'gray', 'gray']

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
# 使用迴圈繪製三張圖
for ax, image, title, cmap in zip(axes, images, titles, cmaps):
    ax.imshow(image, cmap=cmap)
    ax.set_title(title)
plt.show()