# ex2_15.py
# 8進位數字
octal_number = 0o65416

# 轉換成2進位、10進位、16進位
binary = bin(octal_number)   # 轉成2進位
decimal = octal_number      # 轉成10進位
hexadecimal = hex(octal_number)  # 轉成16進位

# 印出結果
print(oct(octal_number), "轉成2進位:", binary)
print(oct(octal_number), "轉成10進位:", decimal)
print(oct(octal_number), "轉成16進位:", hexadecimal)

'''output----------------------------
0o65416 轉成2進位: 0b110101100001110
0o65416 轉成10進位: 27406
0o65416 轉成16進位: 0x6b0e
----------------------------------'''