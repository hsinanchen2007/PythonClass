# ex9_7.py
import numpy as np
# 從 1 到 20 中隨機選擇 10 個不重複的數字
arr = np.random.choice(range(1, 21), size=10, replace=False)
print(arr)

'''output----------------------------------
[10  3  2  4 16 15  7  5  1 13]
----------------------------------------'''