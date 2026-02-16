# ch8_13.py, 利用 raise 主動拋出異常，確保密碼符合條件
def set_password():
    while True:
        try:
            password = input('請輸入密碼（至少8個字元，且包含數字）：')
            if len(password) < 8:
                raise ValueError('長度不足，至少8個字元！')
            if not any(char.isdigit() for char in password):
                raise TypeError('至少包含一個數字！')
            return password  		# 密碼符合要求，回傳
        except ValueError as e:
            print(f'輸入錯誤：{e}')
        except TypeError as e:
            print(f'格式錯誤：{e}')

user_password = set_password()     # 測試set_password()
print(f'密碼設定成功：{user_password}')