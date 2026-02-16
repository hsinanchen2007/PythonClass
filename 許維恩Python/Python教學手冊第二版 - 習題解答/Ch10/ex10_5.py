# ex10_5.py
import numpy as np
# 建立二維陣列 a
a = np.array([
    [12, 10,  0,  9, 12],
    [ 3, 17, 18, -3,  3],
    [ 0,  7,  8,  5,  0]
])
print('二維陣列a=')
print(a)

# (a) 每一橫列的最大值
row_max = np.max(a, axis=1)

# (b) 每一直行的最小值索引
col_min_idx = np.argmin(a, axis=0)

# (c) 每一橫列加總
row_sum = np.sum(a, axis=1)

# (d) 每一直行平均
col_mean = np.mean(a, axis=0)

# (e) 元素值為 0 的列與行索引
zero_indices = np.argwhere(a == 0)
zero_rows = np.unique(zero_indices[:, 0])
zero_cols = np.unique(zero_indices[:, 1])

# (f) 大於 0 的元素總和
positive_sum = np.sum(a[a > 0])

# (g) 最大值的列與行索引
max_idx = np.argwhere(a == np.max(a))[0]  # 只取第一個出現的最大值
max_row_idx, max_col_idx = max_idx

# (h) 提取不包含 0 的直行
no_zero_cols = a[:, ~(a == 0).any(axis=0)]

# (i) 去掉有重複的直行（找出唯一欄）
_, unique_col_indices = np.unique(a, axis=1, return_index=True)
a_unique = a[:, sorted(unique_col_indices)]

# (j) 提取不包含數字 5 的橫列與直行
no_5_rows = a[~np.any(a == 5, axis=1)]
no_5_cols = a[:, ~np.any(a == 5, axis=0)]

# (k) 絕對值為 3 的元素個數
count_abs_3 = np.sum(np.abs(a) == 3)

# 輸出
print(f"(a) 每一橫列的最大值：{row_max}")
print(f"(b) 每一直行的最小值索引：{col_min_idx}")
print(f"(c) 每一橫列加總：{row_sum}")
print(f"(d) 每一直行平均：{col_mean}")
print(f"(e) 值為 0 的列索引：{zero_rows}，行索引：{zero_cols}")
print(f"(f) 大於 0 的元素總和：{positive_sum}")
print(f"(g) 最大值的列索引：{max_row_idx}，行索引：{max_col_idx}")
print(f"(h) 不包含 0 的直行：\n{no_zero_cols}")
print(f"(i) 去掉重複直行後的 a：\n{a_unique}")
print(f"(j) 不包含 5 的橫列：\n{no_5_rows}")
print(f"    不包含 5 的直行：\n{no_5_cols}")
print(f"(k) 絕對值為 3 的元素個數：{count_abs_3}")

'''output-------------------------------------------------------------------------
二維陣列a=
[[12 10  0  9 12]
 [ 3 17 18 -3  3]
 [ 0  7  8  5  0]]
(a) 每一橫列的最大值：[12 18  8]
(b) 每一直行的最小值索引：[2 2 0 1 2]
(c) 每一橫列加總：[43 38 20]
(d) 每一直行平均：[ 5.         11.33333333  8.66666667  3.66666667  5.        ]
(e) 值為 0 的列索引：[0 2]，行索引：[0 2 4]
(f) 大於 0 的元素總和：104
(g) 最大值的列索引：1，行索引：2
(h) 不包含 0 的直行：
[[10  9]
 [17 -3]
 [ 7  5]]
(i) 去掉重複直行後的 a：
[[12 10  0  9]
 [ 3 17 18 -3]
 [ 0  7  8  5]]
(j) 不包含 5 的橫列：
[[12 10  0  9 12]
 [ 3 17 18 -3  3]]
    不包含 5 的直行：
[[12 10  0 12]
 [ 3 17 18  3]
 [ 0  7  8  0]]
(k) 絕對值為 3 的元素個數：3
-------------------------------------------------------------------------------'''