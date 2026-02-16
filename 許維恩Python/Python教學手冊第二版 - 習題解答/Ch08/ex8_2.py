# ex8_2.py
# (a) 找出100的所有因數，並將找出的因數寫入純文字檔ex8_2.txt中，每個因數用逗號隔開。
factors = [i for i in range(1, 101) if 100 % i == 0]
with open('Ch08\\ex8_2.txt', 'w', encoding='utf-8') as f:
    f.write(','.join(map(str, factors)))
print("(a) 已將 100 的因數寫入 ex8_2.txt")

# (b) 開啟ex8_2.txt，讀取寫入的因數，然後計算其總和。
with open('Ch08\\ex8_2.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    numbers = list(map(int, data.split(',')))
    total = sum(numbers)
    print("(b) ex8_2.txt 中的數字總和為：", total)

# (c) 以二進位檔的格式將100的所有因數寫入ex8_2.bin中。
import pickle
with open('Ch08\\ex8_2.bin', 'wb') as f:
    pickle.dump(factors, f)
print("(c) 已將 100 的因數寫入二進位檔 ex8_2.bin")

# (d) 讀取儲存於ex8_2s.bin中的數字，然後計算其總和。
with open('Ch08\\ex8_2.bin', 'rb') as f:
    nums_from_bin = pickle.load(f)
    total_bin = sum(nums_from_bin)
    print("(d) ex8_2.bin 中的數字總和為：", total_bin)

'''output----------------------------------
(a) 已將 100 的因數寫入 ex8_2.txt
(b) ex8_2.txt 中的數字總和為： 217
(c) 已將 100 的因數寫入二進位檔 ex8_2.bin
(d) ex8_2.bin 中的數字總和為： 217
----------------------------------------'''