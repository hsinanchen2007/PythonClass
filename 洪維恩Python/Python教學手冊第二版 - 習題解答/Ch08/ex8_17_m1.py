# ex8_17_m1.py
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10  # 取得數字的最後一位數
        n //= 10  # 去除數字的最後一位
    return total
