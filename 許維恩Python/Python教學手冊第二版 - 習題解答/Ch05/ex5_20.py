# ex5_20.py
def total(n):    
    if n == 1:  # 當 n 為 1 時，傳回 1
        return 1    
    else:   # 遞迴情況：total(n) = n + total(n-1)
        return n + total(n - 1) 

# 測試範例
print('total(5)=', total(5))

'''output--------------------
total(5)= 15
--------------------------'''