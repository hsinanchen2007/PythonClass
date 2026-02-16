# ex12_3.py
import pandas as pd
# (a) 建立 DataFrame 物件 d
arr = [[78, 34, 29, 76],
       [12, 40, 12, 90],
       [33, 10, 65, 20]]
d = pd.DataFrame(arr)
print("(a) 建立的 DataFrame：")
print(d)

# (b) 顯示 d 的後兩筆資料
b_result = d.tail(2)
print("\n(b) 後兩筆資料：")
print(b_result)

# (c) 設定列索引為 a, b, c，欄索引為 w, x, y, z
d.index = ['a', 'b', 'c']
d.columns = ['w', 'x', 'y', 'z']
print("\n(c) 設定新索引後的 DataFrame：")
print(d)

# (d) 提取前3個欄索引（w, x 和 z），轉換為串列
d_columns = d[['w', 'x', 'z']].columns.tolist()
print("\n(d) 前3個欄索引（w, x 和 z）轉為串列：")
print(d_columns)

# (e) 提取列索引為 b，欄索引為 y 的元素
e_result = d.loc['b', 'y']
print("\n(e) 列索引 b、欄索引 y 的元素：", e_result)

# (f) 提取列索引為 c，欄索引為 w 的元素
f_result = d.loc['c', 'w']
print("\n(f) 列索引為 c，欄索引為 w 的元素：",f_result)

# (g) 提取列索引為 a，欄索引為 z 的元素
g_result = d.loc['a', 'z']
print("\n(g) 列索引為 a，欄索引為 z 的元素：", g_result)

'''output------------------------------
(a) 建立的 DataFrame：
    0   1   2   3
0  78  34  29  76
1  12  40  12  90
2  33  10  65  20

(b) 後兩筆資料：
    0   1   2   3
1  12  40  12  90
2  33  10  65  20

(c) 設定新索引後的 DataFrame：
    w   x   y   z
a  78  34  29  76
b  12  40  12  90
c  33  10  65  20

(d) 前3個欄索引（w, x 和 z）轉為串列：
['w', 'x', 'z']

(e) 列索引 b、欄索引 y 的元素： 12

(f) 列索引為 c，欄索引為 w 的元素： 33

(g) 列索引為 a，欄索引為 z 的元素： 76
------------------------------------'''