# ex4_8.py
month = int(input("請輸入月份："))

if 3 <= month <= 5:
    print(f"{month}月為春季")
elif 6 <= month <= 8:
    print(f"{month}月為夏季")
elif 9 <= month <= 11:
    print(f"{month}月為秋季")
else:
    print(f"{month}月為冬季")

'''output--------------------
請輸入月份：3
3月為春季
--------------------------'''