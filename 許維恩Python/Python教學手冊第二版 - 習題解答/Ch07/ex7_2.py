# ex7_2.py
class Sphere:
    def __init__(self, rad):
        self.rad = rad

    def volume(self):
        return round((4 / 3) * 3.14 * (self.rad ** 3), 2)

    def surface_area(self):
        return round(4 * 3.14 * (self.rad ** 2), 2)

# 測試
s0 = Sphere(2)
print(s0.volume())        # 輸出: 33.49
print(s0.surface_area())  # 輸出: 50.24

'''output------
33.49
50.24
------------'''