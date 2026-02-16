# ch10_2.py, printoptions() 搭配 with 區塊
import numpy as np
a = np.sin([0.5, 1, 3])

with np.printoptions(precision = 3):     # 設定小數點精度為 3 位
    print(a)   # 在區塊內的 print() 會使用這個精度

print(a)  # 這裡的 print() 會使用預設精度