# ch10_1.py set_printoptions() 的範例
import numpy as np
a = np.array([1440, 123.89, 0.123])
b = np.sin([0.5, 1, 3])
 
print('預設輸出：')
print(a)
print(b)
 
# 設定新的格式選項
np.set_printoptions(precision = 2, suppress = True)
 
print('套用設定後的輸出：')
print(a)
print(b)
np.set_printoptions(precision = 8, suppress = False)  # 設回預設值