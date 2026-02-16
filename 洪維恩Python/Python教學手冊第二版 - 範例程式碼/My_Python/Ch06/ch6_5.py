# ch6_5.py, 用 hash() 檢查是否出現過
seen = set()				# 空集合

data = ['apple', 'banana', 'apple', 'orange', 'banana']

for item in data:
    h = hash(item)		# 計算item的雜湊
    if h in seen:			# 如果item的雜湊已經存在集合裡
        print(f'重複項目：{item}')
    else:
        seen.add(h)		# 將雜湊加到集合裡