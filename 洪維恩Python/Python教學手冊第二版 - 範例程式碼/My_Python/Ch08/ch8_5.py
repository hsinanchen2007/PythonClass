# ch8_5.py, 寫入與讀取氣溫記錄，並計算平均溫度
with open('temperature.txt', 'w') as f:
    f.writelines([
        '星期一 18 25\n',		# 記得寫上換行符號 \n
        '星期二 20 27\n',
        '星期三 19 26\n',
    ])

# 讀取氣溫並計算每天的平均氣溫
with open('temperature.txt', 'r') as f:
    temps = [line.split() for line in f]  		# 解析每行資料
print(temps)   		# 顯示解析後的資料

for day, t1, t2 in temps:     					# 計算並顯示結果
    avg_temp = (int(t1) + int(t2)) / 2 			# 計算平均氣溫
    print(f'{day}的平均氣溫: {avg_temp:.1f}度')