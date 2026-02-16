# ex5_34.py
# 定義無窮質數產生器 primes()
def primes():
    num = 2  # 從 2 開始
    while True:  # 無窮迴圈，會一直生成質數
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num  # 如果是質數，則產生該質數
        num += 1  # 繼續檢查下一個數字

# 測試primes()函數，使用 next()取得前10個質數
g = primes()  # 建立質數產生器物件
print("前10個質數:")
for _ in range(10):
    print(next(g), end=' ')  # 使用 next() 獲取下一個質數

'''output--------------------
前10個質數:
2 3 5 7 11 13 17 19 23 29
--------------------------'''