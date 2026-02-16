# ex12_10.py
import pandas as pd
# 建立 Series 物件 s
s = pd.Series([34, 35, 12, 88, 99, 16], index=list('abcdef'))

# (a) 將 s 由大到小排序
s_sorted_desc = s.sort_values(ascending=False)
print("(a) s 由大到小排序：")
print(s_sorted_desc)

# (b) 將 s 依其索引從 f 到 a 排序
s_sorted_index_desc = s.sort_index(ascending=False)
print("\n(b) s 依索引從 f 到 a 排序：")
print(s_sorted_index_desc)

'''output---------------------
(a) s 由大到小排序：
e    99
d    88
b    35
a    34
f    16
c    12
dtype: int64

(b) s 依索引從 f 到 a 排序：
f    16
e    99
d    88
c    12
b    35
a    34
dtype: int64
---------------------------'''