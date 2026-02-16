# ex4_20.py
num = int(input("請輸入一個整數: "))
count = 0
# 處理負數情況
if num < 0:
    num = -num

# 計算位數
while num > 0:
    num //= 10
    count += 1

print(f"是{count}個位數的整數")

'''output--------------------
請輸入一個整數: 23983
是5個位數的整數
--------------------------'''