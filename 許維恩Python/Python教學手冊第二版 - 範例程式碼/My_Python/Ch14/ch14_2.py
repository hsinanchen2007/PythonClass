# ch14_2.py, 載入skimage 的內建圖像
from skimage import data
import matplotlib.pyplot as plt

img = data.camera()		# 載入內建灰階圖像
plt.imshow(img, cmap='gray', vmin=0, vmax=255)  # 顯示圖像
plt.axis('off')
plt.show()

print("圖像形狀 shape ：", img.shape)   		# (512, 512)
print("資料型別 dtype ：", img.dtype)    	# uint8
print("圖像總像素數 size：", img.size)     	# 262144
print("圖像前 5x5 像素資料：\n", img[:5, :5])