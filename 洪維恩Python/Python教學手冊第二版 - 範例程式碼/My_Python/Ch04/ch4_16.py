# ch4_16.py, 使用while列印數字遞增的三角形
row = 1  # 控制列數

while row <= 5:  		# 外層迴圈，決定要印出幾列
    col = 1  				
    while col <= row:  	# 內層迴圈，決定當前要印幾個數字
        print(col, end="")     # 印出數字但不換列
        col += 1  		# 讓行數遞增
    print()	# 換列
    row += 1	# 讓列數遞增