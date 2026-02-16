# ex5_6.py
def factor(x):
    factors = []
    divisor = 2
    while x > 1:
        count = 0
        while x % divisor == 0:
            x //= divisor
            count += 1
        if count > 0:
            factors.append([divisor, count])
        divisor += 1
    return factors

# 測試
x=72
print(x,'的質因數分解:',factor(x)) 
x=330
print(x,'的質因數分解:',factor(x)) 

'''output---------------------------------------------
72 的質因數分解: [[2, 3], [3, 2]]
330 的質因數分解: [[2, 1], [3, 1], [5, 1], [11, 1]]
---------------------------------------------------'''