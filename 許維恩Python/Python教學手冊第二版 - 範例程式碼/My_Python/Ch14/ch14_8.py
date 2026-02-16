# ch14_8.py, 自訂 ListedColormap 色表（只顯示第一張圖）
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

palette = np.array([	# 定義自訂色表，需要0到1之間的浮點數
    [1., 0., 0.],   		# 紅色
    [0., 1., 0.],   		# 綠色
    [0., 0., 1.],   		# 藍色
    [0., 0., 0.],   		# 黑色
    [1., 1., 1.]    		# 白色
])
newcmp = ListedColormap(palette)	# 自訂色表
img = np.array([   				# 建立整數圖像陣列
    [9, 7, 3],
    [4, 5, 9],
    [3, 4, 0]
])
plt.figure(figsize=(6, 4))
im = plt.imshow(img, cmap = newcmp, vmin=2)    # 顯示圖像
plt.colorbar(im)
plt.show()