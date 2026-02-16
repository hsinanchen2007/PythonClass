# ch5_4.py, 計算商與餘數的函數
def quo_rem(a, b): 
    quo = a // b  		# quotient (商)
    rem = a % b    	# remainder (餘數)
    return quo, rem	# 同時傳回商和餘數

# 主程式, 測試函數
x, y = 17, 5
q, r = quo_rem(x, y)   # 呼叫quo_rem(x,y),並讓q和r接收傳回值
print(f'{x} 除以 {y} 的商: {q}')
print(f'{x} 除以 {y} 的餘數: {r}')