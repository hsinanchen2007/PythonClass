# ch8_10.py, 使用try-except-else-finally處理異常
try:
    num = int(input('請輸入一個數字：'))
    result = 10 / num    # 可能會發生 ZeroDivisionError
except ZeroDivisionError:
    print('錯誤：除數不能為 0！')
except ValueError:
    print('錯誤：請輸入數字！')
else:
    print(f'計算結果為：{result}')  # 只有當計算成功時才執行
finally:
    print('程式執行結束')  # 無論有無錯誤都會執行