# ex7_8.py
class Temperature:
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit  # 實例屬性 fahrenheit，華氏溫度

    @classmethod
    def from_celsius(cls, celsius):
        fahrenheit = celsius * 9 / 5 + 32  # 攝氏轉華氏公式
        return cls(fahrenheit)  # 回傳一個 Temperature 物件，並傳入計算後的華氏溫度

# 測試
temp = Temperature.from_celsius(25)  # 25°C 轉換為華氏溫度
print(temp.fahrenheit)  # 輸出: 77.0

'''output--------------------
77.0
--------------------------'''