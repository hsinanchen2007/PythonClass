# ex12_9.py
import pandas as pd
import numpy as np
# 根據習題6建立的 DataFrame
d0 = {'Java': [87, 65, 26, 89, 67],
      'C++': [63, 98, 66, 89, 80],
      'Python': [78, 25, 76, 43, 69]}
df = pd.DataFrame(d0)
df.index = ['Tom', 'Bob', 'Tim', 'Wien', 'Lily']

# (a) 將 df 的欄索引順序改為 Python、Java 和 C++，並把結果設給 df2 存放
df2 = df[['Python', 'Java', 'C++']]
print("\n(a) df 的欄索引順序改為 Python、Java 和 C++：")
print(df2)

# (b) 將 df2 的列索引按學生名字的英文字母的次序排序，並把結果設給 df3 存放
df3 = df2.sort_index()
print("\n(b) df2 的列索引按學生名字的英文字母的次序排序：")
print(df3)

# (c) 使用 copy() 函數將 df3 拷貝一份給 df4。於 df4 中，將 Wien 的 Python 成績設為 60。
df4 = df3.copy()
df4.loc['Wien', 'Python'] = 60
print("\n(c) Wien 的 Python 成績設為 60：")
print(df4)

# (d) 將 df3 拷貝一份給 df5。於 df5 中，將每位同學的成績加 10 分，超過 99 分以 99 分計。
df5 = df3.copy()
df5 = df5.apply(lambda x: x + 10).clip(upper=99)  # 每位同學的成績加 10，並超過 99 設為 99
print("\n(d) 每位同學的成績加 10 分，並超過 99 設為 99：")
print(df5)

# (e) 將 df3 拷貝一份給 df6。於 df6 中，將每位同學的成績開根號乘以 10 之後四捨五入到整數，然後列出任一科目少於 60 分的學生。
df6 = df.copy()
df6 = df6.apply(lambda x: np.round(np.sqrt(x) * 10))  # 開根號乘以 10 並四捨五入

# 顯示純文字結果
print("(e) 每位同學的成績開根號乘以 10 之後四捨五入：")
print(df6)
# (e) 列出每個科目少於 60 分的學生（只列出有學生少於 60 分的科目）
print("\n(e) 每個科目少於 60 分的學生：")
for subject in df6.columns:
    students_below_60 = df6[df6[subject] < 60].index
    if len(students_below_60) > 0:
        print(f"{subject}: {', '.join(students_below_60)}")

'''output---------------------------------------
(a) df 的欄索引順序改為 Python、Java 和 C++：
      Python  Java  C++
Tom       78    87   63
Bob       25    65   98
Tim       76    26   66
Wien      43    89   89
Lily      69    67   80

(b) df2 的列索引按學生名字的英文字母的次序排序：
      Python  Java  C++
Bob       25    65   98
Lily      69    67   80
Tim       76    26   66
Tom       78    87   63
Wien      43    89   89

(c) Wien 的 Python 成績設為 60：
      Python  Java  C++
Bob       25    65   98
Lily      69    67   80
Tim       76    26   66
Tom       78    87   63
Wien      60    89   89

(d) 每位同學的成績加 10 分，並超過 99 設為 99：
      Python  Java  C++
Bob       35    75   99
Lily      79    77   90
Tim       86    36   76
Tom       88    97   73
Wien      53    99   99
(e) 每位同學的成績開根號乘以 10 之後四捨五入：
      Java   C++  Python
Tom   93.0  79.0    88.0
Bob   81.0  99.0    50.0
Tim   51.0  81.0    87.0
Wien  94.0  94.0    66.0
Lily  82.0  89.0    83.0

(e) 每個科目少於 60 分的學生：
Java: Tim
Python: Bob
---------------------------------------------'''