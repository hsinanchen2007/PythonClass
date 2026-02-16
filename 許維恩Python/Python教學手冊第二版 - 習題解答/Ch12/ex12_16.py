# ex12_16.py
import pandas as pd

# 創建 DataFrame d
d = pd.DataFrame([[4, 5, 3, 2], [3, 9, 1, 8]], columns=['S', 'M', 'L', 'XL'], index=['a', 'b'])

# (a) 將 d 寫入 CSV 檔（包含列索引和欄索引）
d.to_csv('Ch12\\ex12_16_a.csv')
print("(a) 已將 d 寫入 ex12_16_a.csv 檔案")
# 讀取 ex12_16_a.csv 的內容
d_from_csv_a = pd.read_csv('Ch12\\ex12_16_a.csv', index_col=0)
print("讀取自 ex12_16_a.csv 檔案的內容：")
print(d_from_csv_a)

# (b) 將 d 寫入不包含列索引和欄索引的 CSV 檔
d.to_csv('Ch12\\ex12_16_b.csv', index=False, header=False)
print("(b) 已將 d 寫入 ex12_16_b.csv 檔案")
# 先列出 ex12_16_b.csv 檔案的內容
print("ex12_16_b.csv 檔案內容：")
with open('Ch12\\ex12_16_b.csv', 'r') as file:
    print(file.read())  # 列出檔案內容
# 讀取 ex12_16_b.csv 的內容
g = pd.read_csv('Ch12\\ex12_16_b.csv', header=None)
# 為 g 添加列索引和欄索引
g.columns = ['S', 'M', 'L', 'XL']
g.index = ['a', 'b']
print("讀取自 ex12_16_b.csv 檔案並添加索引後的內容：")
print(g)

# (c) 將 d 寫入 Pickle 檔
d.to_pickle('Ch12\\ex12_16_c.pkl')
print("\n(c) 已將 d 寫入 ex12_16_c.pkl 檔案")
# 讀取 ex12_16_c.pkl 的內容
d_from_pickle = pd.read_pickle('Ch12\\ex12_16_c.pkl')
print("讀取自 ex12_16_c.pkl 檔案的內容：")
print(d_from_pickle)
# 確認寫入的 DataFrame 和讀取的 DataFrame 是否相同
if d.equals(d_from_pickle):
    print("讀取的結果與原始的 DataFrame d 相同")
else:
    print("讀取的結果與原始的 DataFrame d 不相同")

'''output----------------------------
(a) 已將 d 寫入 ex12_16_a.csv 檔案
讀取自 ex12_16_a.csv 檔案的內容：
   S  M  L  XL
a  4  5  3   2
b  3  9  1   8
(b) 已將 d 寫入 ex12_16_b.csv 檔案
ex12_16_b.csv 檔案內容：
4,5,3,2
3,9,1,8

讀取自 ex12_16_b.csv 檔案並添加索引後的內容：
   S  M  L  XL
a  4  5  3   2
b  3  9  1   8

(c) 已將 d 寫入 ex12_16_c.pkl 檔案
讀取自 ex12_16_c.pkl 檔案的內容：
   S  M  L  XL
a  4  5  3   2
b  3  9  1   8
讀取的結果與原始的 DataFrame d 相同
------------------------------------------'''