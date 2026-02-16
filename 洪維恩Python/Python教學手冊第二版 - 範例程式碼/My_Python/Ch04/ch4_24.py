# ch4_24.py, 檢查輸入的串列是否有負數（for-else的寫法）
num = int(input('請輸入一個大於1的數: '))
divisor = 2

while divisor < num:
    if num % divisor == 0:   # 可以被divisor整除
        print(f'{num}不是質數，因為可以被{divisor}整除。')
        break
    divisor += 1
else:
    print(f'{num}是質數！')