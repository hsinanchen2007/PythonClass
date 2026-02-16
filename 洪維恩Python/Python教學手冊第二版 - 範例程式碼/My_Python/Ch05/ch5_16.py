# ch5_16.py, 遞迴函數, 印出倒三角形的圖案
def print_star(n):
    if n<=0:    		# 終止條件：當 n==0 時結束
        return
    print(n*'*')   	# 印出當前那一行的星號
    print_star(n-1)  	# 遞迴：呼叫函數來印出下一行星號

# 測試函數
print_star(5)  