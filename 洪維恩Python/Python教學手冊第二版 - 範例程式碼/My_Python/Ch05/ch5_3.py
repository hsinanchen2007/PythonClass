# ch5_3.py, 將擲骰子的總點數傳出
import random
def roll_dice(n):
    total = 0
    for _ in range(n):
        result = random.randint(1, 6)
        print(f'這次擲骰子的結果是: {result}')
        total += result    # 將點數加總
    return total   # 傳回骰子的總點數

# 主程式，呼叫roll_dice()並印出總和
n = 3    # 擲3次
total_sum = roll_dice(n)
print(f'{n} 次擲骰子的總和是: {total_sum}')