# ex8_11.py
while True:
    try:
        # 請使用者輸入兩個數字
        num1 = input("請輸入第一個數字: ")
        if num1.lower() == 'exit':
            print("程式結束")
            break
        num1 = float(num1)  # 嘗試將輸入轉換為浮點數
        num2 = input("請輸入第二個數字: ")
        if num2.lower() == 'exit':
            print("程式結束")
            break
        # 嘗試將輸入轉換為浮點數
        num2 = float(num2)

        # 計算並顯示除法結果
        result = num1 / num2
        print(f"結果: {num1} ÷ {num2} = {result}")

    except ValueError:
        print("無效輸入，請輸入數字")
    except ZeroDivisionError:
        print("除數不能為零")

'''output--------------------------------------------
請輸入第一個數字: 9
請輸入第二個數字: 5
結果: 9.0 ÷ 5.0 = 1.8
請輸入第一個數字: 6
請輸入第二個數字: 0
除數不能為零
請輸入第一個數字: w
無效輸入，請輸入數字
請輸入第一個數字: 5
請輸入第二個數字: i
無效輸入，請輸入數字
請輸入第一個數字: 5
請輸入第二個數字: 3
結果: 5.0 ÷ 3.0 = 1.6666666666666667
請輸入第一個數字: exit
程式結束
---------------------------------------------------'''