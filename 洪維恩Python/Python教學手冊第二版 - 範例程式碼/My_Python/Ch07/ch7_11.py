# ch7_11.py, 不使用多型的範例
class Animal: 			# 父類別Animal
    pass

class Dog(Animal): 		# 子類別Dog
    pass

class Cat(Animal): 		# 子類別Cat
    pass

# 測試
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    if isinstance(animal, Dog):
        print('汪汪！')
    elif isinstance(animal, Cat):
        print('喵喵！')
    else:
        print('動物發出聲音')