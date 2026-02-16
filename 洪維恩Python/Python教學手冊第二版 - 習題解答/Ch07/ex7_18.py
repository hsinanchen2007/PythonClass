# ex7_18.py
class Year:
    def __init__(self, year):
        self.__year = year  # 設定私有屬性 __year

    # Getter
    @property
    def year(self):
        return self.__year  # 取得 __year 的值

    # Setter
    @year.setter
    def year(self, value):
        self.__year = value  # 設定 __year 的值

    # 判斷是否為閏年
    def isleap(self):
        if (self.__year % 4 == 0 and self.__year % 100 != 0) or (self.__year % 400 == 0):
            return True
        return False

# 測試
y0 = Year(2024)
print(y0.isleap())  # 輸出: True
print(y0.year)      # 輸出: 2024
y0.year = 2023
print(y0.isleap())  # 輸出: False

'''output------
True
2024
False
------------'''