# ex10_16.py
import numpy as np

# 定義陣列和 x
a = np.array([78, 22, 65, 87, 12, 98, 63, 79])
x = 57

# (a) 使用 for 迴圈查找離 x 最近的數
min_diff = float('inf')
closest_value_for = None
for value in a:
    diff = abs(value - x)
    if diff < min_diff:
        min_diff = diff
        closest_value_for = value
print("(a) 使用 for 迴圈找到的離 x 最近的數：", closest_value_for)

# (b) 不使用 for 迴圈，利用 NumPy 廣播來找出離 x 最近的數
diffs = np.abs(a - x)  # 計算每個元素與 x 的差的絕對值
closest_value_no_for = a[np.argmin(diffs)]  # 找出最小的差對應的元素
print("(b) 不使用 for 迴圈找到的離 x 最近的數：", closest_value_no_for)

'''output-----------------------------------
(a) 使用 for 迴圈找到的離 x 最近的數： 63
(b) 不使用 for 迴圈找到的離 x 最近的數： 63
-----------------------------------------'''