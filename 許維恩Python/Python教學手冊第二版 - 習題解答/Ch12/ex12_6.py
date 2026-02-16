# ex12_6.py
import pandas as pd
# (a) 以字典 d0 建立 DataFrame 物件 df
d0 = {'Java': [87, 65, 26, 89, 67],
      'C++': [63, 98, 66, 89, 80],
      'Python': [78, 25, 76, 43, 69]}
df = pd.DataFrame(d0)
print("(a) 建立的 DataFrame：")
print(df)

# (b) 設定列索引為 ['Tom', 'Bob', 'Tim', 'Wien', 'Lily']
df.index = ['Tom', 'Bob', 'Tim', 'Wien', 'Lily']
print("\n(b) 設定列索引後的 DataFrame：")
print(df)

'''output---------------------------
(a) 建立的 DataFrame：
   Java  C++  Python
0    87   63      78
1    65   98      25
2    26   66      76
3    89   89      43
4    67   80      69

(b) 設定列索引後的 DataFrame：
      Java  C++  Python
Tom     87   63      78
Bob     65   98      25
Tim     26   66      76
Wien    89   89      43
Lily    67   80      69
---------------------------------'''