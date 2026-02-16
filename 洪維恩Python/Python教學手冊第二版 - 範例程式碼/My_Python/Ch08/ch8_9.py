# ch8_9.py, 使用if-else來避免輸入錯誤
num = input('請輸入一個數字：')

if num.isdigit() or (num.startswith('-') and num[1:].isdigit()):  
    num = int(num)
    if num == 0:   # 檢查是否為 0
        print('錯誤：除數不能為 0！')
    else:
        result = 10 / num
        print(f'計算結果為：{result}')
else:
    print('錯誤：請輸入數字！')