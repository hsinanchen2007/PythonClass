# ex8_13.py,
def check_age():
    try:
        # 讓使用者輸入年齡
        age = int(input("請輸入年齡: "))
        
        # 檢查年齡是否小於18
        if age < 18:
            # 如果年齡小於18，使用 raise 拋出錯誤
            raise ValueError("年齡不能小於18")
        
        # 如果年齡大於或等於18，印出年齡
        print(f"年齡為 {age} 歲")
    
    except ValueError as e:
        # 如果捕捉到 ValueError，顯示錯誤訊息
        print(e)

# 呼叫函數來檢查年齡
check_age()

'''output--------
請輸入年齡: 12
年齡不能小於18
--------------'''

'''output--------
請輸入年齡: 25
年齡為 25 歲
--------------'''