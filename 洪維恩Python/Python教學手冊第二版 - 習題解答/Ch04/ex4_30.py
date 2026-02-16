# ex4_30.py
while True:
    password = input("請輸入密碼：")    
    is_valid = True

    if len(password) < 6:
        print("密碼長度至少 6 個字元")
        is_valid = False

    for char in password:
        if not ('0' <= char <= '9' or 'A' <= char <= 'Z' or 'a' <= char <= 'z'):
            print("密碼只能包含英文字母或數字")
            is_valid = False
            break  # 若已經發現不符合，就不需要繼續檢查
    
    if is_valid:
        print("密碼設定成功")
        break

'''output--------------------
請輸入密碼：@1234  
密碼長度至少 6 個字元
密碼只能包含英文字母或數字
請輸入密碼：123456
密碼設定成功
--------------------------'''