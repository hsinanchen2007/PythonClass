# ch5_14.py, 使用global關鍵字
count = 0  			# 全域變數，記錄函數呼叫次數
def call_function():
    global count		# 指定使用全域變數 count
    count += 1
    print('函數已被呼叫', count, '次')

call_function()
call_function()
call_function()
