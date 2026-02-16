# ex7_4.py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"嗨, 我是 {self.name}，{self.age} 歲.")

# 測試
p = Person('Alice', 21)
p.greet()  # 輸出: 嗨, 我是 Alice，21 歲.

'''output-----------------
嗨, 我是 Alice，21 歲.
-----------------------'''