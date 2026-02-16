# ex2_20.py
number = int(input("請輸入一個整數: "))      # 從鍵盤讀入一個整數
binary = bin(number)                        # 將該整數轉換為2進位
print(f"{number} 的二進位表示是: {binary}")   # 列印二進位結果

'''output--------------
請輸入一個整數: 6
6 的二進位表示是: 0b110
--------------------'''