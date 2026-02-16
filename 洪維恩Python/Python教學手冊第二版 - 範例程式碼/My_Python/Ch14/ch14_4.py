# ch14_4.py, 不同 threshold 對二值化結果的影響
from skimage import data
import matplotlib.pyplot as plt
import numpy as np

img = data.camera()   # 讀取圖像
thresholds = [50, 128, 200] # 設定三個不同的 threshold
fig, axes = plt.subplots(1, 3, figsize=(12, 4)) # 建立子圖

# 對每個 threshold 分別二值化並顯示
for ax, th in zip(axes, thresholds):
    binary_img = img > th       # 大於th為True，小於等於為False
    ax.imshow(binary_img, cmap='gray')
    ax.set_title(f"Threshold = {th}")
plt.show()