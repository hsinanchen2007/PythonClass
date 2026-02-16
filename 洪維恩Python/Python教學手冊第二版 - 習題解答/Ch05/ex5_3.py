# ex5_3.py
def isprime(x):
    if x < 2:  # 小於 2 的數不是質數
        return False
    for i in range(2, int(x ** 0.5) + 1):  # 只需檢查到 sqrt(x)
        if x % i == 0:
            return False
    return True

# 測試
n=17
print(n,'是質數嗎？',isprime(n))
n=18
print(n,'是質數嗎？',isprime(n))

'''output--------------------
17 是質數嗎？ True
18 是質數嗎？ False
--------------------------'''