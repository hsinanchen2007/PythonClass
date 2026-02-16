# ch5_15.py, 遞迴函數,階乘
def fact(n):
    if n>1:        			# 遞迴 
        return n*fact(n-1)		# 傳回 n 乘以 n-1 的階乘
    else:
        return 1   			# 終止條件，當 n=1 時傳回 1

# 測試函數
print(fact(4))   # 輸出 24