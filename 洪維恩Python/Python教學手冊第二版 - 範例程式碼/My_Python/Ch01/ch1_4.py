# ch1_4.py, 語意錯誤
price = 100
discount = 20
final_price = price + discount  # 應該是減去折扣，但這裡錯用了加法
print('折扣後價格=', final_price)