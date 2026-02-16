# ex12_15.py
import pandas as pd
# 創建 Series 物件 s
s = pd.Series([34, 76, 33, 78], index=list('abcd'))

print("s的內容：")
print(s)

# (a) 將 Series 寫入 CSV 檔案，檔名為 ex12_15.csv，並讀取檔案
s.to_csv('Ch12\\ex12_15.csv', header=True)
print('已將 s 寫入 ex12_15.csv 檔案')
s_from_csv = pd.read_csv('Ch12\\ex12_15.csv', index_col=0)  # 使用 index_col=0 設定第一欄為索引
print("讀取自 ex12_15.csv 檔案的內容：")
print(s_from_csv)

# (b) 將 Series 寫入 Pickle 檔案，檔名為 ex12_15.pkl，並讀取檔案
s.to_pickle('Ch12\\ex12_15.pkl')
print('\n已將 s 寫入 ex12_15.pkl 檔案')
s_from_pickle = pd.read_pickle('Ch12\\ex12_15.pkl')
print("讀取自 ex12_15.pkl 檔案的內容：")
print(s_from_pickle)

'''output----------------------------
s的內容：
a    34
b    76
c    33
d    78
dtype: int64
已將 s 寫入 ex12_15.csv 檔案
讀取自 ex12_15.csv 檔案的內容：
    0
a  34
b  76
c  33
d  78

已將 s 寫入 ex12_15.pkl 檔案
讀取自 ex12_15.pkl 檔案的內容：
a    34
b    76
c    33
d    78
dtype: int64
----------------------------------'''