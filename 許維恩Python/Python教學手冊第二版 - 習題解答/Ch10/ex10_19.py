# ex10_19.py
import numpy as np

# (a) 使用 for 迴圈建立陣列
arr_for = np.zeros((4, 5), dtype=int)  # 初始化 4x5 的陣列
for r in range(4):
    for c in range(5):
        arr_for[r, c] = 2 * r + c  # 使用公式填充陣列
print("(a) 使用 for 迴圈建立的陣列：")
print(arr_for)

# (b) 使用串列生成式來建立陣列
arr_list_comprehension = np.array([[2 * r + c for c in range(5)] for r in range(4)])
print("(b) 使用串列生成式建立的陣列：")
print(arr_list_comprehension)

# (c) 使用 NumPy 廣播來建立陣列
r = np.arange(4).reshape((4, 1))  # 建立行索引陣列
c = np.arange(5)  # 建立列索引陣列
arr_broadcast = 2 * r + c  # 使用廣播運算來生成結果
print("(c) 使用 NumPy 廣播建立的陣列：")
print(arr_broadcast)

'''output---------------------------------------
(a) 使用 for 迴圈建立的陣列：
[[ 0  1  2  3  4]
 [ 2  3  4  5  6]
 [ 4  5  6  7  8]
 [ 6  7  8  9 10]]
(b) 使用串列生成式建立的陣列：
[[ 0  1  2  3  4]
 [ 2  3  4  5  6]
 [ 4  5  6  7  8]
 [ 6  7  8  9 10]]
(c) 使用 NumPy 廣播建立的陣列：
[[ 0  1  2  3  4]
 [ 2  3  4  5  6]
 [ 4  5  6  7  8]
 [ 6  7  8  9 10]]
---------------------------------------------'''