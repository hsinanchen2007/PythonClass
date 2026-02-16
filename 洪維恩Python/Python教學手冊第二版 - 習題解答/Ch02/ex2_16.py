# ex2_16.py
# 2進位數字
bin_number = 0b1001001

# 轉換成8進位、10進位、16進位
octal = oct(bin_number)   # 轉成8進位
decimal = bin_number      # 轉成10進位
hexadecimal = hex(bin_number)  # 轉成16進位

# 印出結果
print(bin(bin_number), "轉成8進位:", octal)
print(bin(bin_number), "轉成10進位:", decimal)
print(bin(bin_number), "轉成16進位:", hexadecimal)

'''output----------------------------
0b1001001 轉成8進位: 0o111
0b1001001 轉成10進位: 73
0b1001001 轉成16進位: 0x49
----------------------------------'''