# ch4_10.py, 找出串列中的最大值
numbers = [3, 7, 9, 2]	# 定義一個串列
max_value = numbers[0]	# 假設索引0的數字為最大值

for num in numbers:  		# 走訪串列中的每個數字
    if num > max_value:  	# 如果發現更大的數字
        max_value = num   	# 更新最大值變數

print('最大值為:', max_value)  # 印出最大值