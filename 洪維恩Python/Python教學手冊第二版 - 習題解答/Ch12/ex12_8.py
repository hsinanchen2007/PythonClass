# ex12_8.py
import pandas as pd
# 以字典 d0 建立 DataFrame 物件 df
d0 = {'Java': [87, 65, 26, 89, 67],
      'C++': [63, 98, 66, 89, 80],
      'Python': [78, 25, 76, 43, 69]}
df = pd.DataFrame(d0,index = ['Tom', 'Bob', 'Tim', 'Wien', 'Lily'])
print("建立的 DataFrame：")
print(df)

# (a) 列出 Python 大於等於 60 分的學生
a_result = df[df['Python'] >= 60]
print("\n(a) Python 大於等於 60 分的學生：")
print(a_result)

# (b) 列出所有科目都大於等於 60 分的學生
b_result = df[(df['Java'] >= 60) & (df['C++'] >= 60) & (df['Python'] >= 60)]
print("\n(b) 所有科目都大於等於 60 分的學生：")
print(b_result)

# (c) 列出 Python 小於 60 分的同學所有科目的成績
c_result = df[df['Python'] < 60]
print("\n(c) Python 小於 60 分的同學所有科目成績：")
print(c_result)

# (d) 列出 Tim 所有大於等於 60 分的科目
d_result = df.loc['Tim'][df.loc['Tim'] >= 60]
print("\n(d) Tim 所有大於等於 60 分的科目：")
print(d_result)

# (e) 列出所有學生都及格的科目
e_result = df.columns[(df >= 60).all()]
# 以純文字顯示所有符合條件的科目
print("\n(e) 所有學生都及格的科目：",end=" ")
if not e_result.empty:
    print(", ".join(e_result))  # 如果有多個科目，會用逗號分隔顯示
else:
    print("沒有所有學生都及格的科目")

'''output-----------------------------------
建立的 DataFrame：
      Java  C++  Python
Tom     87   63      78
Bob     65   98      25
Tim     26   66      76
Wien    89   89      43
Lily    67   80      69

(a) Python 大於等於 60 分的學生：
      Java  C++  Python
Tom     87   63      78
Tim     26   66      76
Lily    67   80      69

(b) 所有科目都大於等於 60 分的學生：
      Java  C++  Python
Tom     87   63      78
Lily    67   80      69

(c) Python 小於 60 分的同學所有科目成績：
      Java  C++  Python
Bob     65   98      25
Wien    89   89      43

(d) Tim 所有大於等於 60 分的科目：
C++       66
Python    76
Name: Tim, dtype: int64

(e) 所有學生都及格的科目： C++
-----------------------------------------'''