# ex7_1.py
class Window:
    def __init__(self, width=10, height=5):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# 測試
w0 = Window()
w1 = Window(12, 8)

print(w0.area())  # 輸出: 50
print(w1.area())  # 輸出: 96

'''output------------------------------
50
96
------------------------------------'''