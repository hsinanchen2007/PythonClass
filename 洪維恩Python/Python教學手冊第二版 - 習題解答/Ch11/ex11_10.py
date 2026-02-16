# ex11_10.py
import numpy as np
import matplotlib.pyplot as plt

# 判斷質數的函數
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 計算小於等於 n 的質數個數
def prime_count(n):
    return sum(1 for i in range(2, n+1) if is_prime(i))

# 生成 2 到 100 之間的 n 值
n_values = np.arange(2, 101)
f_values = np.array([prime_count(n) for n in n_values])

# 繪製散點圖
plt.figure(figsize=(8, 5))
plt.scatter(n_values, f_values, color='blue', label=r'$f(n)$')
plt.title('Number of Primes Less Than or Equal to n $f(n)$')
plt.xlabel('n')
plt.ylabel('f(n)')
plt.grid(True)
plt.legend()

plt.show()      # 顯示圖形

'''output---------------------

---------------------------'''