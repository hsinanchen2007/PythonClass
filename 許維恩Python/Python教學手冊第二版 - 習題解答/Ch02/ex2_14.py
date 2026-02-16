# ex2_14.py
# 10進位數字
decimal_number = 1024

# 轉換成2進位、8進位、16進位
binary = bin(decimal_number)   # 轉成2進位
octal = oct(decimal_number)    # 轉成8進位
hexadecimal = hex(decimal_number)  # 轉成16進位

# 印出結果
print(decimal_number, "轉成2進位:", binary)
print(decimal_number, "轉成8進位:", octal)
print(decimal_number, "轉成16進位:", hexadecimal)

'''output----------------------
1024 轉成2進位: 0b10000000000
1024 轉成8進位: 0o2000
1024 轉成16進位: 0x400
----------------------------'''