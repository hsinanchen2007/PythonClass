# ch14_16.py, 邊緣偵測
import matplotlib.pyplot as plt
from skimage import data
from skimage.feature import canny	# 載入canny() 函數

coins = data.coins()				# 讀取範例圖像
fig, axes = plt.subplots(1, 3, figsize=(9, 4))

for i, ax in enumerate(axes):		# 使用不同sigma進行邊緣偵測
    edges = canny(coins, sigma=i)
    ax.imshow(edges, cmap='gray')
    ax.set_title(f'sigma={i}')
    ax.axis('off')
plt.show()