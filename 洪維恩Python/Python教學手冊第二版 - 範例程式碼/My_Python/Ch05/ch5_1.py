# ch5_1.py, 模擬擲骰子程式 
import random
def roll_dice():
    num = random.randint(1, 6)  
    print(f'骰出的數字是: {num}')

roll_dice()   # 呼叫函數
roll_dice()   # 呼叫函數