# ex10_10.py
import numpy as np
# 建立陣列
a = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])
print('陣列a=')
print(a)

# (a) 計算每一行（axis=0）的平均值
mean_cols = np.mean(a, axis=0)

# (b) 計算每一列（axis=1）的中位數
median_rows = np.median(a, axis=1)

# (c) 計算整個陣列的標準差
std_all = np.std(a)

# (d) 計算每一列的第 25 百分位數
percentile_25_rows = np.percentile(a, 25, axis=1)

# 輸出結果
print(f"(a) 每一行的平均值：{mean_cols}")
print(f"(b) 每一列的中位數：{median_rows}")
print(f"(c) 整個陣列的標準差：{std_all}")
print(f"(d) 每一列的第 25 百分位數：{percentile_25_rows}")

'''output------------------------------------
陣列a=
[[10 20 30]
 [40 50 60]
 [70 80 90]]
(a) 每一行的平均值：[40. 50. 60.]
(b) 每一列的中位數：[20. 50. 80.]
(c) 整個陣列的標準差：25.81988897471611
(d) 每一列的第 25 百分位數：[15. 45. 75.]
------------------------------------------'''