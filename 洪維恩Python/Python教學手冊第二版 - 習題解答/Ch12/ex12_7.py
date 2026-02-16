# ex12_7.py
import pandas as pd
# 以字典 d0 建立 DataFrame 物件 df
d0 = {'Java': [87, 65, 26, 89, 67],
      'C++': [63, 98, 66, 89, 80],
      'Python': [78, 25, 76, 43, 69]}
df = pd.DataFrame(d0,index = ['Tom', 'Bob', 'Tim', 'Wien', 'Lily'])
print("建立的 DataFrame：")
print(df)

# (a) 提取 Tim 和 Wien 的所有成績
a_result = df.loc[['Tim', 'Wien']]
print("\n(a) Tim 和 Wien 的所有成績：")
print(a_result)

# (b) 提取所有學生的 Python 成績
b_result = df['Python']
print("\n(b) 所有學生的 Python 成績：")
print(b_result)

# (c) 提取 Lily 的 Python 成績
c_result = df.loc['Lily', 'Python']
print("\n(c) Lily 的 Python 成績：",c_result)

# (d) 提取 Tom 的 Python 和 C++ 成績
d_result = df.loc['Tom', ['Python', 'C++']]
print("\n(d) Tom 的 Python 和 C++ 成績：")
print(d_result)

# (e) 提取所有學生的 Python 和 Java 成績
e_result = df[['Python', 'Java']]
print("\n(e) 所有學生的 Python 和 Java 成績：")
print(e_result)

# (f) 計算每個學生的平均成績
f_result = df.mean(axis=1)
print("\n(f) 每個學生的平均成績：")
print(f_result)

# (g) 計算每個科目的平均成績
g_result = df.mean(axis=0)
print("\n(g) 每個科目的平均成績：")
print(g_result)

'''output----------------------------------
建立的 DataFrame：
      Java  C++  Python
Tom     87   63      78
Bob     65   98      25
Tim     26   66      76
Wien    89   89      43
Lily    67   80      69

(a) Tim 和 Wien 的所有成績：
      Java  C++  Python
Tim     26   66      76
Wien    89   89      43

(b) 所有學生的 Python 成績：
Tom     78
Bob     25
Tim     76
Wien    43
Lily    69
Name: Python, dtype: int64

(c) Lily 的 Python 成績： 69

(d) Tom 的 Python 和 C++ 成績：
Python    78
C++       63
Name: Tom, dtype: int64

(e) 所有學生的 Python 和 Java 成績：
      Python  Java
Tom       78    87
Bob       25    65
Tim       76    26
Wien      43    89
Lily      69    67

(f) 每個學生的平均成績：
Tom     76.000000
Bob     62.666667
Tim     56.000000
Wien    73.666667
Lily    72.000000
dtype: float64

(g) 每個科目的平均成績：
Java      66.8
C++       79.2
Python    58.2
dtype: float64
----------------------------------------'''