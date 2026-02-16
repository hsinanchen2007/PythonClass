# ex4_9.py
sec = int(input("請輸入秒數："))

if sec < 0 or sec >= 86400:
    print("輸入的秒數不正確，請確保它小於86,400。")
else:
    hours = sec // 3600  # 計算小時
    sec %= 3600  # 剩餘的秒數
    minutes = sec // 60  # 計算分鐘
    seconds = sec % 60  # 計算秒數

    # 格式化輸出，保證兩位數
    print(f"{hours:02d}小時{minutes:02d}分{seconds:02d}秒")

'''output--------------------
請輸入秒數：14865
04小時07分45秒
--------------------------'''