# ex7_13.py
# 定義父類別 Animal
class Animal:
    def make_sound(self):
        print("動物發出聲音")

# 定義子類別 Dog，繼承自 Animal
class Dog(Animal):
    def make_sound(self):
        print("汪汪")

# 測試
dog = Dog()
dog.make_sound()  # 輸出: 汪汪

'''output----
汪汪
----------'''