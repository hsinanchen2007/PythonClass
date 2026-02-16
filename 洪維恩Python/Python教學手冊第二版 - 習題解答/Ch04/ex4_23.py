# ex4_23.py
# 讀取輸入的數字
num = int(input("請輸入一個整數: "))

# 判斷是否為質數
if num < 2:
    print(f"{num} 不是質數")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} 不是質數")
            break
    else:
        print(f"{num} 是質數")

'''output-------------
請輸入一個整數: 17
17 是質數
-------------------'''