# ex10_8.py
def prime_list(n):
    primes = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

# 測試：列出小於 30 的所有質數
print('小於 30 的所有質數:',prime_list(30))

'''output--------------------------------------------------
小於 30 的所有質數: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
--------------------------------------------------------'''