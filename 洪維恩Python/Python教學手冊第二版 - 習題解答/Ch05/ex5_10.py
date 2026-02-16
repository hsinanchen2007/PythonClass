# ex5_10.py
def factors(n):
    # 回傳小於n的因數
    return [i for i in range(1, n) if n % i == 0]

def is_perfect(n):
    # 判斷是否為完美數
    return sum(factors(n)) == n

# 找出4個位數以下的完美數
perfect_numbers = [n for n in range(1, 10000) if is_perfect(n)]
print('4個位數以下的完美數：',perfect_numbers)

'''output----------------------------------
4個位數以下的完美數： [6, 28, 496, 8128]
----------------------------------------'''