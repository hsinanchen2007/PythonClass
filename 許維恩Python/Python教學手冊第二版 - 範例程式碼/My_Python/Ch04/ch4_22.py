# ch4_22.py, 檢查輸入的串列是否有負數（沒有else的寫法）
numbers=eval(input('請輸入一個串列: '))
found=False  			# 用found來記錄是否有負數被找到
for num in numbers:
    if num<0: 
        print('找到負數')
        found=True		# 找到負數
        break			# 跳離for迴圈
if not found:			# 如果沒有找到負數
    print('都是正數') 