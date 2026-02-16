# ch12_6.py，刪除與插入列或欄
import pandas as pd
data={'Species': ['Cat', 'Dog'], 			# 建立資料表
      'Weight': [4.2, 9.1],
      'Health': ['Good', 'Poor']}
index = ['CoCo', 'Toby']
df=pd.DataFrame(data, index=index)
print(f"原始資料：")
print(df)

df.drop(columns='Health', inplace=True) 	# 刪除 健康 欄
print("\n刪除 Health 欄後：")
print(df)

df.insert(1, 'Age', [3, 5]) 				# 插入新的欄位 年齡
print("\n插入 Age 欄後：")
print(df)