# C:\python_pkg\ex8_16_math2.py
def prime_factors(n):
    factors = []
    divisor = 2  # 從最小的質數 2 開始分解
    while n >= divisor:
        while n % divisor == 0:  # 如果能整除，則是質因數
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
