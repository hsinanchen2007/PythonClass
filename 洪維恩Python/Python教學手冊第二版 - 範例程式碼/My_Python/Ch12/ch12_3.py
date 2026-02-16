# ch12_3.py, 茶葉重量價格查詢
import pandas as pd
df = pd.DataFrame({				# 建立 DataFrame
    '100g': [300, 425, 450],
    '150g': [400, 612, 824],
    '200g': [750, 830, 1399]
}, index=['Black Tea', 'Green Tea', 'OolongTea'])

def query_price(tea: str, weight: str):
    price = df.loc[tea, weight]  	# 直接從DataFrame查詢
    print(f"{tea}, {weight} 價格是 {price}")
    return price

query_price("Green Tea", "100g")  	# 測試查詢
query_price("Black Tea", "200g")   	# 測試查詢
query_price("OolongTea", "150g")   	# 測試查詢