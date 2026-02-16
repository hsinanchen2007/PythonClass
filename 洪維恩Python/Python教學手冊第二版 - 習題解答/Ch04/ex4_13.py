# ex4_13.py
n = int(input("請輸入一個整數："))
result = 1

# 計算 n 的階乘
for i in range(1, n + 1):
    result *= i

print(f"{n} 的階乘是 {result}")

'''output-------------------------
請輸入一個整數：5
5 的階乘是 120
-------------------------------'''