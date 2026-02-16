# ch7_4.py, 傳遞物件到實例函數（兩隻寵物之間的賽跑）
import random
class Pet:
    def __init__(self, name):
        self.name = name
    def race(self, other):   # 可接收一個Pet物件
        my_speed = random.randint(1, 10)  		# self物件的速度
        other_speed = random.randint(1, 10)		# other物件的速度
        winner = self.name if my_speed > other_speed else other.name
        return f'{winner} 跑贏了~'

pet1 = Pet('小橘貓')		# 建立 pet1 物件
pet2 = Pet('虎斑貓')		# 建立 pet2 物件
result = pet1.race(pet2)	# 傳遞 pet2 到 race() 並進行比賽
print(result)