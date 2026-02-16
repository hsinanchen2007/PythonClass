# ex5_33.py
# 定義質數產生器 primes(n)
def primes(n):
    # 設定 2 為最小的質數
    for num in range(2, n + 1):
        is_prime = True
        # 檢查 num 是否為質數
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        # 如果是質數，則 yield 該數
        if is_prime:
            yield num

# 測試 primes(n) 函數，設 n = 20
n = 20
print(f"小於等於{n}的質數:")
print(list(primes(n)))  # 將產生的質數轉換為列表並顯示

'''output------------------------
小於等於20的質數:
[2, 3, 5, 7, 11, 13, 17, 19]
------------------------------'''