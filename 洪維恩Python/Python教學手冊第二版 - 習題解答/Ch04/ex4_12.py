# ex4_12.py
price = int(input("請輸入購買金額："))

# 檢查金額是否大於100
if price > 100:
    print("購買金額不能超過100元")
else:
    change = 100 - price  # 顧客付款100元，找零錢的金額

    # 計算每個面額的硬幣數量
    if change >= 50:
        coin_50 = change // 50
        change %= 50
    else:
        coin_50 = 0

    if change >= 10:
        coin_10 = change // 10
        change %= 10
    else:
        coin_10 = 0

    if change >= 5:
        coin_5 = change // 5
        change %= 5
    else:
        coin_5 = 0

    coin_1 = change  # 剩餘的都是1元硬幣

    print(f"50元{coin_50}枚，10元{coin_10}枚，5元{coin_5}枚，1元{coin_1}枚")

'''output-------------------------
請輸入購買金額：21
50元1枚，10元2枚，5元1枚，1元4枚
-------------------------------'''