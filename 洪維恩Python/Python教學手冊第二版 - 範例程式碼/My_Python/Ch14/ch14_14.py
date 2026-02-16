# ch14_14.py, 縮放與旋轉的練習
import matplotlib.pyplot as plt
from skimage import data
from skimage.transform import rescale, resize, rotate

img = data.coffee()    # 讀取咖啡杯圖像，形狀為 (400, 600, 3)
img_rescaled=rescale(img, scale=0.25, channel_axis=2)  # 縮小25%
img_resized=resize(img,(210, 210))    # 調整成210x210大小
img_rotated=rotate(img,angle=45, resize=True, cval=1) # 旋轉45度

images = [img_rescaled, img_resized, img_rotated]
titles = ['Rescale 0.25x', 'Resize to 210x210', 'Rotate 45°']

fig, ax = plt.subplots(1, 3, figsize=(15, 5))
for image, axis, title in zip(images, ax, titles):
    axis.imshow(image)
    axis.set_title(title)
plt.show()