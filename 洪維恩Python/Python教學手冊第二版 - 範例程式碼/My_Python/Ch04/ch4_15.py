# ch4_15.py, 使用 while 猜測數字
import random
target = random.randint(1, 10)   # 隨機產生1到10的數字
guess = 0  # 用來存放使用者的猜測值

while guess != target:  	# 當猜錯時，持續執行
    guess = int(input('猜一個1到10之間的數字: '))
    if guess < target:
        print('太小了！請再試一次')
    elif guess > target:
        print('太大了！請再試一次')
print('恭喜你，猜對了！')