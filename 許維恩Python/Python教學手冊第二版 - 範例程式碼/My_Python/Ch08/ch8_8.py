# ch8_8.py, 使用pickle模組的範例
import pickle
# 要儲存的字典資料
data = {'name': 'Alice', 'age': 25, 'scores': [90, 85, 88]}

with open('data.pkl', 'wb') as f:  # 將資料存入 pickle 檔案
    pickle.dump(data, f)			# 將data轉成二進位後寫入檔案f

with open('data.pkl', 'rb') as f:  # 從 pickle 檔案讀取資料
    loaded_data = pickle.load(f)

print(loaded_data) 