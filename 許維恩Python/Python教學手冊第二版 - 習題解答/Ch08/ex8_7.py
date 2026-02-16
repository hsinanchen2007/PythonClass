# ex8_7.py
from io import StringIO, BytesIO
import csv
import pickle
# (a) 使用 StringIO 將數字資料寫入記憶體，並找出最大值
csv_data = '75,87,86,19,69\n78,65,12,77,90'
f0 = StringIO(csv_data) # 使用 StringIO 寫入記憶體

# 讀取資料並轉換為二維串列
data = [list(map(int, row)) for row in csv.reader(f0, delimiter=',')]
print("(a) 讀取的資料：")   # 印出讀取的資料
print(data)

# 找出最大值
max_value = max(max(row) for row in data)
print("資料中的最大值:", max_value)

# (b) 使用 BytesIO 將 [{3, 5}, 'Python', (64, 1024)] 寫入記憶體，並將其還原
data_bytes = [{3, 5}, 'Python', (64, 1024)]
# 使用 pickle 將資料轉換成 bytes 物件
bytes_data = pickle.dumps(data_bytes)
# 使用 BytesIO 寫入記憶體
f0_bytes = BytesIO(bytes_data)
# 從記憶體讀取並反序列化
read_data = pickle.load(f0_bytes)
# 顯示還原後的資料
print("\n(b) 讀取並還原的資料:")
print(read_data)

'''output-------------------------------------------------------
(a) 讀取的資料：
[[75, 87, 86, 19, 69], [78, 65, 12, 77, 90]]
資料中的最大值: 90

(b) 讀取並還原的資料:
[{3, 5}, 'Python', (64, 1024)]
-------------------------------------------------------------'''