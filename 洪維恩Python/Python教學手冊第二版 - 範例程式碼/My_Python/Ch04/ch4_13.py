# ch4_13.py, 產生數字遞減的三角形圖案
for r in range(0,5):  # 外層迴圈，控制列數，r從0遞增到4
    for c in range(1,6-r):		# 內層迴圈，控制每列要印出幾個數字
        print(c, end="")  		# 印出數字
    print()  # 換列，準備印下一列