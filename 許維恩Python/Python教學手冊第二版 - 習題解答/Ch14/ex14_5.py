# ex14_5.py
import numpy as np
import matplotlib.pyplot as plt

# 建立 2×4×3 的陣列
img = np.zeros((2, 4, 3), dtype=np.uint8)

# 定義顏色 (RGB格式)
colors = [
    (255, 0, 0),    # 紅
    (0, 0, 0),      # 黑
    (255, 255, 255),# 白
    (0, 255, 0),    # 綠
    (128, 128, 128),# 灰
    (0, 0, 255),    # 藍
    (0, 255, 255),  # 青
    (255, 255, 0)   # 黃
]

# 將顏色填入img
for idx, color in enumerate(colors):
    row = idx // 4
    col = idx % 4
    img[row, col] = color

# 顯示
plt.imshow(img)
plt.axis('off')
plt.title('2x4 Color Image')
plt.show()

'''output-----

-----------'''