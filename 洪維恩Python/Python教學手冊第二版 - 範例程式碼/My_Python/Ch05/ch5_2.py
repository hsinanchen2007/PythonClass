# ch5_2.py, 帶有一個參數的擲骰子程式
import random
def roll_dice(n):
    for _ in range(n):
        num = random.randint(1, 6) 
        print(f'骰出的數字是: {num}')

roll_dice(3)  # 擲骰子 3 次 