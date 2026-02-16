# ch4_18.py, 限制密碼的輸入次數
password = 'python123'  # 正確密碼
attempts = 0  # 記錄輸入次數

while attempts < 3:  # 最多允許3次輸入
    pwd = input('請輸入密碼: ')  # 使用者輸入密碼
    if pwd == password:
        print('密碼正確，登入成功！')
        break  # 結束迴圈
    else:
        print('密碼錯誤！')
        attempts += 1  # 增加錯誤次數

if attempts == 3:
    print('輸入錯誤3次，系統鎖定！')