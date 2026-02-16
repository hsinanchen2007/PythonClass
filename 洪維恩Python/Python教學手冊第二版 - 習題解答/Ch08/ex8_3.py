# ex8_3.py
# 讀取文字檔並轉成數字列表
numbers = []
with open('Ch08\\ex8_3.txt', 'r', encoding='utf-8') as f:
    print("檔案內容如下：")
    for line in f:
        print(line.strip())  # 印出每一行內容（去掉換行符號）
        line_numbers = list(map(int, line.split()))
        numbers.extend(line_numbers)

# 找最大值與最小值
max_num = max(numbers)
min_num = min(numbers)
print("\n文字檔中的最大值為：", max_num)
print("文字檔中的最小值為：", min_num)

'''output--------------------
檔案內容如下：
23 45 23 65
44 56 88 21
50 67 89 12

文字檔中的最大值為： 89
文字檔中的最小值為： 12
--------------------------'''