# ex12_11.py
import pandas as pd
# 建立 DataFrame 物件 d
d = pd.DataFrame([[4, 5, 3], [3, 9, 1]], columns=['M', 'L', 'XL'], index=['a', 'b'])

# (a) 將索引為 a 之列的元素值由大到小排序，然後依以此結果排序 d 的每一欄
sorted_row_a = d.loc['a'].sort_values(ascending=False)
d_sorted_by_row_a = d[sorted_row_a.index]  # 依排序後的索引順序重新排列 d 的每一欄
print("(a) 排序後的 d:")
print(d_sorted_by_row_a)

# (b) 將 d 以欄索引的字元編碼順序來排序（編碼小的排在前面）
d_sorted_by_column = d[sorted(d.columns)]  # 使用字母順序來排序欄位
print("\n(b) 按欄索引字元編碼順序排序的 d:")
print(d_sorted_by_column)

# (c) 將 d 的列索引依字元編碼的順序反向排序（編碼大的排在前面）
d_sorted_by_row_reverse = d.sort_index(ascending=False)
print("\n(c) 按列索引字元編碼反向排序的 d:")
print(d_sorted_by_row_reverse)

'''output---------------------------
(a) 排序後的 d:
   L  M  XL
a  5  4   3
b  9  3   1

(b) 按欄索引字元編碼順序排序的 d:
   L  M  XL
a  5  4   3
b  9  3   1

(c) 按列索引字元編碼反向排序的 d:
   M  L  XL
b  3  9   1
a  4  5   3
---------------------------------'''