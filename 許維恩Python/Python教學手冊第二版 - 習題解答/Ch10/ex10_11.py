# ex10_11.py
import numpy as np
# 原始資料
a = np.array([12, 7, 23, 76, 23, 77, 54, 33, 98])

# 篩選偶數
even_numbers = a[a % 2 == 0]

# 將偶數排序（從小到大）
sorted_even = np.sort(even_numbers)

# 輸出結果
print(f"偶數：{even_numbers}")
print(f"排序後的偶數：{sorted_even}")

'''output---------------------------
偶數：[12 76 54 98]
排序後的偶數：[12 54 76 98]
---------------------------------'''