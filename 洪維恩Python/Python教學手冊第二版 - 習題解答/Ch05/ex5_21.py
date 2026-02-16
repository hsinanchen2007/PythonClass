# ex5_21.py
def r_pow(base, n):    
    if n == 0:  # 當 n 為 0 時，返回 1
        return 1    
    else:   # 遞迴情況：計算 base 的 n 次方
        return base * r_pow(base, n - 1)

base = 2
n = 8
result = r_pow(base, n)
print(base, '的', n, '次方 =', result)

'''output--------------------
2 的 8 次方 = 256
--------------------------'''