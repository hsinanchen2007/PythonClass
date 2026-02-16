# ch8_6.py CSV檔的處理
import csv
with open('temperature.csv', 'w', newline="", encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Day', 't1', 't2'])  # 寫入標題
    writer.writerows([
        ['星期一', 18, 25],
        ['星期二', 20, 27],
        ['星期三', 19, 26],
    ])
# 讀取CSV檔案並計算平均
with open('temperature.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # 跳過標題行
    for day, t1, t2 in reader:
        avg_temp = (int(t1) + int(t2)) / 2  # 計算平均
        print(f'{day}的平均氣溫: {avg_temp:.1f} 度')