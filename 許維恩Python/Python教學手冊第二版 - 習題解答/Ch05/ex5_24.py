# ex5_24.py
# (a) 使用 def 定義 sign(x) 函數
def sign(x):
    if x >= 0:
        return 1
    else:
        return -1

# (b) 使用 lambda 改寫 sign(x)
sign_lambda = lambda x: 1 if x >= 0 else -1

# (c) 使用 lambda 函數對 lst 進行判別
lst = [9, -3, 8, 2, 1, -1, -4]
result = [sign_lambda(x) for x in lst]

# (d) 設計 sign2(x)，考慮 x > 0、x == 0 和 x < 0
sign2 = lambda x: 1 if x > 0 else (0 if x == 0 else -1)

# 測試輸出
print("sign(10) =", sign(10))
print("sign(-5) =", sign(-5)) 
print("sign_lambda(10) =", sign_lambda(10))
print("sign_lambda(-5) =", sign_lambda(-5))
print("lst 判別結果 =", result)
print("sign2(10) =", sign2(10))
print("sign2(0) =", sign2(0))
print("sign2(-5) =", sign2(-5)) 

'''output-------------
sign(10) = 1
sign(-5) = -1
sign_lambda(10) = 1
sign_lambda(-5) = -1
lst 判別結果 = [1, -1, 1, 1, 1, -1, -1]
sign2(10) = 1
sign2(0) = 0
sign2(-5) = -1
-------------------'''