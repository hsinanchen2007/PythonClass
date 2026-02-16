# ex12_1.py
import pandas as pd
lst = [95, 77, 98, 65]  # 建立 Series
s = pd.Series(lst)

# (a) 查詢 s 的型別、形狀和元素個數
print("(a) 型別、形狀和元素個數")
print("型別：", type(s))
print("形狀：", s.shape)
print("元素個數：", s.size)

# (b) 提取索引為 0 和 2 的元素
print("\n(b) 索引為 0 和 2 的元素")
print(s[[0, 2]])

# (c) 提取除了第一個以外的所有元素
print("\n(c) 除了第一個以外的所有元素")
print(s[1:])

# (d) 將索引改為 a, b, c, d
print("\n(d) 將索引改為 'a', 'b', 'c', 'd'")
s.index = ['a', 'b', 'c', 'd']
print(s)

# (e) 提取奇數的元素
print("\n(e) 奇數的元素")
print(s[s % 2 == 1])

# (f) 將偶數設為 100
print("\n(f) 將偶數設為 100")
s[s % 2 == 0] = 100
print(s)

'''output------------------------------------
(a) 型別、形狀和元素個數
型別： <class 'pandas.core.series.Series'>
形狀： (4,)
元素個數： 4

(b) 索引為 0 和 2 的元素
0    95
2    98
dtype: int64

(c) 除了第一個以外的所有元素
1    77
2    98
3    65
dtype: int64

(d) 將索引改為 'a', 'b', 'c', 'd'
a    95
b    77
c    98
d    65
dtype: int64

(e) 奇數的元素
a    95
b    77
d    65
dtype: int64

(f) 將偶數設為 100
a     95
b     77
c    100
d     65
dtype: int64
------------------------------------------'''