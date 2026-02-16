# ex4_31.py
string = input("請輸入一個字串：")
is_all_digits = True  # 假設字串全為數字

for char in string:
    if not ('0' <= char <= '9'):  # 檢查是否為數字
        is_all_digits = False
        break

if is_all_digits:
    print(string)
else:
    print("輸入的數包含不合法的字元")

'''output--------------------
請輸入一個字串：123@abc
輸入的數包含不合法的字元
--------------------------'''

'''output--------------------
請輸入一個字串：123456
123456
--------------------------'''