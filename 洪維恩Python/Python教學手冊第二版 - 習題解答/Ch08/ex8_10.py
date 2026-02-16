# ex8_10.py
import math
try:
    user_input = input("請輸入一個數字：")
    number = float(user_input)  # 嘗試轉換為數字

    if number < 0:
        print("不能輸入負數")
    else:
        result = math.sqrt(number)
        print("輸入正確")
        print(f"開根號結果為：{result:.2f}")

except ValueError:
    print("必須輸入數字")

'''output------------------------
請輸入一個數字: -8
不能輸入負數
------------------------------'''

'''output------------------------
請輸入一個數字：52
輸入正確
開根號結果為：7.21
------------------------------'''