# ex14_10.py
import numpy as np
import matplotlib.pyplot as plt
from skimage.data import camera

# 讀取 camera 圖像，並正規化到 [0, 1]
img = camera() / 255.0  # camera 圖像大小為 (512, 512)

# 圖像切割的行數與列數
num_blocks_vertical = 4
num_blocks_horizontal = 8

# 區塊的大小
block_height = img.shape[0] // num_blocks_vertical
block_width = img.shape[1] // num_blocks_horizontal

# (a) 將圖像切割成 4×8 個區塊，並顯示出來
fig, axs = plt.subplots(num_blocks_vertical, num_blocks_horizontal, figsize=(12, 8))
for i in range(num_blocks_vertical):
    for j in range(num_blocks_horizontal):
        # 計算區塊的範圍
        start_x = i * block_height
        end_x = (i + 1) * block_height
        start_y = j * block_width
        end_y = (j + 1) * block_width
        # 擷取區塊
        block = img[start_x:end_x, start_y:end_y]
        # 顯示每個區塊
        axs[i, j].imshow(block, cmap='gray')
        axs[i, j].axis('off')

# 顯示切割後的圖像
fig.suptitle("Original Blocks", fontsize=16)
plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.show()

# (b) 計算每個區塊的平均值，並以平均值取代該區塊內的每個像素
reconstructed_img = np.zeros_like(img)
for i in range(num_blocks_vertical):
    for j in range(num_blocks_horizontal):
        # 計算區塊的範圍
        start_x = i * block_height
        end_x = (i + 1) * block_height
        start_y = j * block_width
        end_y = (j + 1) * block_width
        # 擷取區塊
        block = img[start_x:end_x, start_y:end_y]
        # 計算區塊的平均值
        block_mean = np.mean(block)
        # 用平均值填充區塊
        reconstructed_img[start_x:end_x, start_y:end_y] = block_mean

# (c) 將取代後的區塊組合成一張圖像並顯示出來
plt.imshow(reconstructed_img, cmap='gray')
plt.title("Reconstructed Image (Averaged Blocks)")
plt.axis('off')
plt.show()

'''output------------------------------------

------------------------------------------'''