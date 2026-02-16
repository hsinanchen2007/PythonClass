# ex14_11.py
import numpy as np
import matplotlib.pyplot as plt
from skimage.data import astronaut

# 讀取 astronaut 彩色圖像
img = astronaut()  # shape = (512, 512, 3)

# 切割參數
num_blocks_vertical = 8   # 高度方向切成 8 個區塊
num_blocks_horizontal = 4 # 寬度方向切成 4 個區塊
block_height = img.shape[0] // num_blocks_vertical  # 每個區塊高度 = 64
block_width = img.shape[1] // num_blocks_horizontal # 每個區塊寬度 = 128

# (a) 將圖像切割成 8×4 區塊，並顯示出來
fig, axs = plt.subplots(num_blocks_vertical, num_blocks_horizontal, figsize=(10, 16))
blocks = []  # 儲存切割的區塊
for i in range(num_blocks_vertical):
    row_blocks = []
    for j in range(num_blocks_horizontal):
        start_x = i * block_height
        end_x = (i + 1) * block_height
        start_y = j * block_width
        end_y = (j + 1) * block_width

        block = img[start_x:end_x, start_y:end_y, :]
        row_blocks.append(block)

        axs[i, j].imshow(block)
        axs[i, j].axis('off')
    blocks.append(row_blocks)
plt.suptitle("(a) 8×4 Blocks of Astronaut", fontsize=16)
plt.tight_layout()
plt.subplots_adjust(top=0.95)
plt.show()

# (b) 將切割結果重新組合為原圖
reconstructed = np.zeros_like(img)
for i in range(num_blocks_vertical):
    for j in range(num_blocks_horizontal):
        start_x = i * block_height
        end_x = (i + 1) * block_height
        start_y = j * block_width
        end_y = (j + 1) * block_width
        reconstructed[start_x:end_x, start_y:end_y, :] = blocks[i][j]
plt.imshow(reconstructed)
plt.title("(b) Reconstructed Image from Blocks")
plt.axis('off')
plt.show()

'''output---------------------------

---------------------------------'''