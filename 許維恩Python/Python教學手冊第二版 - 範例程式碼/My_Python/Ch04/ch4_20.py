# ch4_20.py, 使用continue跳過負數進行累加
numbers = [10, -5, 3, -1, 7, -6, 2]   # 包含正數和負數的串列
total_sum = 0   		# 初始化總和變數

for num in numbers:	# 走訪串列中的每個數字
    if num < 0:
        continue		# 如果數字是負數，跳過這次迭代
    total_sum += num	# 將正數加到總和中

print('正數的總和是:', total_sum) 