# ex7_15.py
# 定義 Car 類別
class Car:
    def __init__(self, color):
        self.color = color  # 設定顏色屬性

    def show(self):
        print(f'color={self.color}')  # 輸出顏色

# 定義 Truck 類別，繼承自 Car
class Truck(Car):
    def __init__(self, doors, owner, color):
        super().__init__(color)  # 呼叫父類別的 __init__() 設定 color 屬性
        self.doors = doors  # 設定車門數量
        self.owner = owner  # 設定車主

    def show(self):
        print(f'doors={self.doors}, owner={self.owner}, color={self.color}')  # 輸出車門數、車主和顏色

# 測試
truck = Truck(4, 'Alice', 'Red')
truck.show()  # 輸出: doors=4, owner=Alice, color=Red

'''output----------------------------------
doors=4, owner=Alice, color=Red
----------------------------------------'''