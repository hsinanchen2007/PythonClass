# ch5_13.py, 全域變數與區域變數
x = 10    	# 全域變數  
y = 20    	# 全域變數 
def my_function():
    x = 5		# 區域變數（會覆蓋掉全域變數）
    print(f'函數內部 x = {x}, y = {y}')

my_function()
print('函數外部 x =', x) 