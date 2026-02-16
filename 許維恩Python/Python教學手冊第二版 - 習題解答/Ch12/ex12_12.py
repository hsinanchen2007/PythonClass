# ex12_12.py
import pandas as pd
# 建立 DataFrame 物件 d
d = pd.DataFrame([[40, 50, 36], [12, 19, 21]], columns=['a', 'b', 'c'])

# (a) 分別計算 d 的每一列和每一欄的平均值
row_means = d.mean(axis=1)  # 每一列的平均
column_means = d.mean(axis=0)  # 每一欄的平均
print("(a) 每一列的平均值:")
print(row_means)
print("\n每一欄的平均值:")
print(column_means)

# (b) 計算 d 中所有元素的加總
total_sum = d.sum().sum()  # 先計算每欄加總，再將各欄加總起來
print("\n(b) 所有元素的加總:", total_sum)

# (c) 計算 d 每一欄之元素的標準差
column_std = d.std(axis=0)  # 每一欄的標準差
print("\n(c) 每一欄的標準差:")
print(column_std)

'''output--------------------
(a) 每一列的平均值:
0    42.000000
1    17.333333
dtype: float64

每一欄的平均值:
a    26.0
b    34.5
c    28.5
dtype: float64

(b) 所有元素的加總: 178

(c) 每一欄的標準差:
a    19.798990
b    21.920310
c    10.606602
dtype: float64
--------------------------'''