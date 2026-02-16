# ex4_5.py
grade = int(input("請輸入成績："))  # 讀取成績

# 判斷等級
if grade >= 90:
    level = "A"
elif grade >= 80:
    level = "B"
elif grade >= 70:
    level = "C"
elif grade >= 60:
    level = "D"
else:
    level = "F"

print(f"{grade}分，等級為{level}")  # 印出結果

'''output--------------------
請輸入成績：78
78分，等級為C
--------------------------'''