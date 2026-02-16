# ex14_6.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# 色表順序：紅、黑、白、綠、灰、藍、青、黃
colors = [
    (255, 0, 0),       # 紅
    (0, 0, 0),         # 黑
    (255, 255, 255),   # 白
    (0, 255, 0),       # 綠
    (128, 128, 128),   # 灰
    (0, 0, 255),       # 藍
    (0, 255, 255),     # 青
    (255, 255, 0)      # 黃
]

# 將 RGB 轉為 0~1 之間的值
colors = np.array(colors) / 255.0

# 建立自訂色表
cmap = ListedColormap(colors)

# 建立圖像資料（對應上方文字）
image = np.array([
    [0, 6, 2, 3],   # 紅 青 白 綠
    [4, 5, 6, 7],   # 灰 藍 青 黃
    [2, 1, 3, 4]    # 白 黑 綠 灰
])

# 繪圖
plt.imshow(image, cmap=cmap)
plt.xticks([])  # 不顯示 x 軸刻度
plt.yticks([])  # 不顯示 y 軸刻度
plt.title("Custom Colormap Image")
plt.show()

'''output-----

-----------'''