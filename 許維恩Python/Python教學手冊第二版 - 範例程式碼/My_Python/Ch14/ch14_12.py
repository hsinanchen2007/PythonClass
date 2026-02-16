# ch14_12.py, # 彩色圖像的裁切與像素值的設定
import numpy as np
from skimage import img_as_ubyte

# 原始浮點數陣列（範圍0~1）
imgF = np.array([[0.00, 0.12, 0.65],  
                   [0.76, 0.20, 1.00]])

# 用運算公式計算
manual = np.clip(np.round(255 * imgF), 0, 255).astype(np.uint8)
 
# 使用 img_as_ubyte() 自動轉換
ubyte_img = img_as_ubyte(imgF)   
 
print(manual)
print(ubyte_img)