# ch4_11.py, 走訪range()並計算偶數的平均
total = 0  	# 用來存儲偶數的總和
count = 0  	# 存放偶數的個數

for num in range(1, 11):	# 走訪 1 到 10（不含 11）
    if num % 2 == 0:		# 判斷是否為偶數
        total += num		# 加總偶數
        count += 1			# 計算偶數個數

average = total / count   # 計算平均值
print('偶數的平均值:', average)