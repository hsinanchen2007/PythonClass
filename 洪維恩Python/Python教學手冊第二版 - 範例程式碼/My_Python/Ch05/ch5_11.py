# ch5_11.py, 位置參數與指名參數
def order_drink(drink, size, sugar=90, ice=100):
    print(f'品名: {drink}, 容量: {size}, 糖分: {sugar}, 冰塊: {ice}')
  
order_drink('珍奶', '大杯', 50, 30)   			 # 使用位置參數
order_drink(size='大杯', drink='綠茶', sugar=70)  # 使用指名參數
order_drink('紅茶', '小杯', ice = 50)   # 位置參數+指名參數+預設值