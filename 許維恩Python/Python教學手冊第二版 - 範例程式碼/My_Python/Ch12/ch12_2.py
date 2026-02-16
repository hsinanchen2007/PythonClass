# ch12_2.py, 寵物資訊管理
import pandas as pd  
data = {'Name': ['Luna', 'Mimi', 'Coco'],
        'Type': ['狗', '貓', '兔'],
        'Age': [3, None, 5],            # Mimi的年齡缺失
        'Weight': [None, 4.3, 2.6]}    # Luna的體重缺失
df = pd.DataFrame(data) 		# 建立DataFrame，其中部分數據缺失
print("原始寵物資料：")
print(df.to_string())

if df['Age'].isna().all():
    df['Age'] = 0       		# 如果整欄都是NaN，就用0
else:
    df['Age'] = df['Age'].fillna(df['Age'].mean())

if df['Weight'].isna().all():
    df['Weight'] = 0    		# 如果整欄都是NaN，就用0
else:
    df['Weight'] = df['Weight'].fillna(df['Weight'].mean())

print("\n填補缺失值後的寵物資料：")     # 處理後的DataFrame
print(df.to_string()) 