# ch14_3.py, float 圖像與 cmap='gray' 顯示差異
from skimage import data
import matplotlib.pyplot as plt

img = data.camera()/255  # 將圖像轉為0-1範圍 
fig, axes = plt.subplots(1, 3, figsize=(10, 4))   # 建立子圖
axes[0].imshow(img)
axes[1].imshow(img, cmap='gray', vmin=0, vmax=255)
axes[2].imshow(img, cmap='gray', vmin=0, vmax=1)
plt.show()  