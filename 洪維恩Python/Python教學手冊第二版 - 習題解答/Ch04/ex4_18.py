# ex4_18.py
num = int(input("請輸入一個整數: "))
for digit in str(num)[::-1]:
    print(digit, end="")

'''output--------------------
請輸入一個整數: 12345
54321
--------------------------'''