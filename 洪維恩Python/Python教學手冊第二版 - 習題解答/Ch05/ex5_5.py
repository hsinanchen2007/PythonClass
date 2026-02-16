# ex5_5.py
def prime_factors(x):
    factors = []
    divisor = 2
    while x > 1:
        if x % divisor == 0:
            if divisor not in factors:
                factors.append(divisor)
            x //= divisor
        else:
            divisor += 1
    return factors

# 測試
x=72
print(x,'的質因數:',prime_factors(x)) 
x=150
print(x,'的質因數:',prime_factors(x)) 

'''output--------------------
72 的質因數: [2, 3]
150 的質因數: [2, 3, 5]
--------------------------'''