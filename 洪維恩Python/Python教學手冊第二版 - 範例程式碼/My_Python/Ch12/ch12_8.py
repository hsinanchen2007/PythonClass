# ch12_8.py, 統計不同品牌汽車的月銷售資料
import pandas as pd
data = {
    'Toyota': 97077,     
    'Honda': 23692,        
    'Nissan': 17397,    
    'Mitsubishi': 13932}
df = pd.DataFrame(data, index=['Total']).T

df['Avg_Month'] = df['Total'] // 12	# 計算平均月銷量
total_sales = df['Total'].sum()		# 計算所有車子總銷量

# 計算佔有率
df['Share%'] = ((df['Total'] / total_sales) * 100).round(2)
print(df)