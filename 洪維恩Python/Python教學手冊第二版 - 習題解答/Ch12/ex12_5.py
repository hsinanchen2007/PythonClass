# ex12_5.py
import pandas as pd
s = pd.Series([77, 34, 78, 20, 12, 35]) # 原始 Series
print("(原始 s):")
print(s)

# (a) 提取索引為 0、2 和 3 的元素
a_result = s[[0, 2, 3]]
print("\n(a) 索引為 0、2、3 的元素：")
print(a_result)

# (b) 提取後 3 個元素
b_result = s[-3:]
print("\n(b) 後 3 個元素：")
print(b_result)

# (c) 提取大於 60 的元素
c_result = s[s > 60]
print("\n(c) 大於 60 的元素：")
print(c_result)

# (d) 提取偶數並求平均
even_values = s[s % 2 == 0]
d_result = even_values.mean()
print("\n(d) 偶數平均值：",d_result)

# (e) 計算 s + s^2、s * s^2 和 s^2 / (2 * s)
s_squared = s ** 2      # s 的平方
print("\n(s 的平方 s^2):")
print(s_squared)
# (e-1) s + s^2
e1 = s + s_squared
print("\n(e1) s + s^2：")
print(e1)
# (e-2) s * s^2
e2 = s * s_squared
print("(e2) s * s^2：")
print(e2)
# (e-3) s^2 / (2 * s)
e3 = s_squared / (2 * s)
print("(e3) s^2 / (2 * s)：")
print(e3)

'''output--------------------
(原始 s):
0    77
1    34
2    78
3    20
4    12
5    35
dtype: int64

(a) 索引為 0、2、3 的元素：
0    77
2    78
3    20
dtype: int64

(b) 後 3 個元素：
3    20
4    12
5    35
dtype: int64

(c) 大於 60 的元素：
0    77
2    78
dtype: int64

(d) 偶數平均值： 36.0

(s 的平方 s^2):
0    5929
1    1156
2    6084
3     400
4     144
5    1225
dtype: int64

(e1) s + s^2：
0    6006
1    1190
2    6162
3     420
4     156
5    1260
dtype: int64
(e2) s * s^2：
0    456533
1     39304
2    474552
3      8000
4      1728
5     42875
dtype: int64
(e3) s^2 / (2 * s)：
0    38.5
1    17.0
2    39.0
3    10.0
4     6.0
5    17.5
dtype: float64
--------------------------'''