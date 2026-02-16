# ch5_12.py, 使用任意個數的參數
def sum_args(a, b, *args, c = 0):
    print(f"a = {a}, b = {b}, args = {args}, c= {c}", end=", ")
    print(f'sum = {a + b + sum(args) + c}')
 
sum_args(1, 2, 3, 4, 5)  		# *args = (3, 4, 5)，c 用預設值 0
sum_args(1, 2, 3, 4, c=5)  	# *args = (3, 4)，c = 5
sum_args(1, b=2, c=5)     		# *args = ()，c = 5
# sum_args(1, b=2, 3, c=5)		# 錯誤：指名參數後不可在位置參數之前
# sum_args(a=1, 2, 3, c=4)     # 錯誤：指名參數後不可在位置參數之前