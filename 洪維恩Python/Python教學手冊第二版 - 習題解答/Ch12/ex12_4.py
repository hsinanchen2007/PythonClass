# ex12_4.py
import pandas as pd

# (a) 以 data 建立一個 DataFrame 物件 d
data = {
    'Name': ['Tom', 'Jerry', 'Mickey'],
    'Age': [3, 5, 2],
    'Weight': [4.2, 8.0, 5.5],
    'Species': ['Cat', 'Mouse', 'Mouse']}
d = pd.DataFrame(data)
print("(a) 建立的 DataFrame：")
print(d)

# (b) 顯示 d 的前兩筆資料
b_result = d.head(2)
print("\n(b) 前兩筆資料：")
print(b_result)

# (c) 設定列索引為 ['a', 'b', 'c']，欄索引保持不變（也可以重新指定）
d.index = ['a', 'b', 'c']
d.columns = ['Name', 'Age', 'Weight', 'Species']
print("\n(c) 設定新索引後的 DataFrame：")
print(d)

# (d) 提取欄索引為 ['Name', 'Age'] 的資料，並轉換為串列（轉為巢狀串列）
d_selected = d[['Name', 'Age']].values.tolist()
print("\n(d) Name 和 Age 欄轉成串列：")
print(d_selected)

# (e) 提取列索引為 b，欄索引為 Weight 的元素
e_result = d.loc['b', 'Weight']
print("\n(e) 列索引 b、欄索引 Weight 的元素：", e_result)

'''output------------------------------------
(a) 建立的 DataFrame：
     Name  Age  Weight Species
0     Tom    3     4.2     Cat
1   Jerry    5     8.0   Mouse
2  Mickey    2     5.5   Mouse

(b) 前兩筆資料：
    Name  Age  Weight Species
0    Tom    3     4.2     Cat
1  Jerry    5     8.0   Mouse

(c) 設定新索引後的 DataFrame：
     Name  Age  Weight Species
a     Tom    3     4.2     Cat
b   Jerry    5     8.0   Mouse
c  Mickey    2     5.5   Mouse

(d) Name 和 Age 欄轉成串列：
[['Tom', 3], ['Jerry', 5], ['Mickey', 2]]

(e) 列索引 b、欄索引 Weight 的元素： 8.0
------------------------------------------'''