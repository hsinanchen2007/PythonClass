# ch7_10.py, 多型的範例
class Animal:					# 父類別Animal
    def speak(self):
        print('動物發出聲音')

class Dog(Animal): 			# 子類別Dog
    def speak(self):
        print('汪汪！')

class Cat(Animal): 			# 子類別Cat
    def speak(self):
        print('喵喵！')

# 測試多型
animals = [Dog(), Cat(), Animal()]  # 建立不同型別的物件
for animal in animals:
    animal.speak()  		# 不同型別的物件呼叫相同名稱的函數