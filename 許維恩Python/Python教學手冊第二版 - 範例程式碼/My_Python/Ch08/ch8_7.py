# ch8_7.py 二進位檔的處理
matrix = [
    [12, 34, 56, 78],
    [90, 23, 45, 67],
    [89, 21, 43, 65]
]

# 將矩陣寫入二進位檔案
with open('matrix.bin', 'wb') as file:
    for row in matrix:
        file.write(bytes(row))   	# 每列轉換為二進位並寫入檔案

# 從二進位檔案讀取矩陣
r_matrix = []
with open('matrix.bin', 'rb') as file:
    for _ in range(3):  			# 矩陣有3列
        row = list(file.read(4))  	# 讀取4個bytes(每列4個數字)
        r_matrix.append(row)
        print(row)  				# 印出每列的內容