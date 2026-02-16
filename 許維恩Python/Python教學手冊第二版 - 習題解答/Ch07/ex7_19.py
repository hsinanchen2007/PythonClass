# ex7_19.py
class Rectangle:
    def __init__(self, width, height):
        self._width = width  # 初始寬度
        self._height = height  # 初始高度

    # Getter: 計算面積
    @property
    def area(self):
        return self._width * self._height

    # Setter: 設定寬度，確保不為負數
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 0:
            print("寬度不能為負數，設置為 0")
            self._width = 0
        else:
            self._width = value

    # Setter: 設定高度，確保不為負數
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            print("高度不能為負數，設置為 0")
            self._height = 0
        else:
            self._height = value

# 測試
rect = Rectangle(5, 10)
print(rect.area)   # 輸出: 50
rect.width = -3     # 輸出: 寬度不能為負數，設置為 0
rect.height = -2    # 輸出: 高度不能為負數，設置為 0
print(rect.area)    # 輸出: 0

'''output-------------------
50
寬度不能為負數，設置為 0
高度不能為負數，設置為 0
0
-------------------------'''