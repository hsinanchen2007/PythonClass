# ex8_6.py
import csv
# (a) 使用 csv 模組寫入資料到 ex8_6.csv
students = [
    ['John', 18, 85],
    ['Mary', 19, 90],
    ['Jeff', 17, 78]
]

# 開啟檔案並寫入資料，並指定編碼為 UTF-8
with open('Ch08\\ex8_6.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['姓名', '年齡', '成績'])  # 寫入標題列
    writer.writerows(students)  # 寫入學生資料

# (b) 讀取 ex8_6.csv 並顯示學生資料，並指定編碼為 UTF-8
with open('Ch08\\ex8_6.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # 跳過標題列
    for row in reader:
        name, age, score = row
        print(f"姓名: {name}, 年齡: {age}, 成績: {score}")

'''output---------------------------------------------------
(a) 0 到 1 之間的亂數 = 0.6258793658882768
(b) 從 'Significant' 中隨機抽取 3 個字元 = ['S', 'f', 't']
(c) 1 到 6 之間的整數亂數 = 2
(d) 1 到 10 之間的偶數隨機挑選一個數 = 10
(e) 介於 -1 到 1 之間的浮點數亂數 = 0.6510928183881299
---------------------------------------------------------'''