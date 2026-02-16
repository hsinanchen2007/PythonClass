# ex14_9.py
import matplotlib.pyplot as plt
from skimage.data import chelsea

# 讀取 chelsea 圖像
img = chelsea()

# 對調紅色 (R) 和藍色 (B) 通道
img_swapped = img.copy()
img_swapped[:, :, 0] = img[:, :, 2]  # 將藍色通道賦值給紅色通道
img_swapped[:, :, 2] = img[:, :, 0]  # 將紅色通道賦值給藍色通道

# 顯示原始圖像與對調後的圖像
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

axs[0].imshow(img)
axs[0].set_title("Original Image (Chelsea)")
axs[0].axis('off')

axs[1].imshow(img_swapped)
axs[1].set_title("Image with Red and Blue Channels Swapped")
axs[1].axis('off')

plt.tight_layout()
plt.show()

'''output說明--------------------------------
紅色和藍色通道對調後，圖像的色調將發生變化，
通常這樣會使圖像顯得有些異常，
紅色會變成藍色，藍色會變成紅色。
----------------------------------------'''