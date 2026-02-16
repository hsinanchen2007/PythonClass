# ch5_10.py, 參數的預設值
def introduce(name, age = 18, city = '台北'):
    print(f'Hi，我是 {name}，今年 {age} 歲，來自 {city}')

# 測試不同的參數組合
introduce('Sandy')			# 預設年齡 18，城市為台北
introduce('Tippi', 19)		# 省略城市，年齡變 19
introduce('Junie', 20, '台中')	# 指定所有參數