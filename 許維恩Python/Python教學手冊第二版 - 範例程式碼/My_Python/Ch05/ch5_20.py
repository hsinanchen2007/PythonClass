# ch5_20.py, 郵局取號機的 Python 版本
tickets = [101, 102, 103]  # 可迭代物件（等待辦理業務的號碼）
machine = iter(tickets)    # 取號機（迭代器）負責依序叫號

while True:     # 郵局開始叫號
    current_ticket = next(machine, None)  # 先嘗試取下一個號碼
    if current_ticket is None:  # 沒有號碼就直接結束，不顯示提示
        print("沒有號碼了，停止提取號碼。")
        break
    input("請按 Enter 鍵取號...")  # 等待用戶按下 Enter
    print('請', current_ticket, '到櫃檯')  # 依序提取號碼