# ch10_5.py, 步數紀錄分析
import numpy as np
steps = np.array([8500, 9000, 7600, 8800, 5300])
days = np.array(['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
 
print('平均步數：', np.mean(steps))			
print('中位數：', np.median(steps))
print('標準差：', np.std(steps))
 
# 最多與最少步數及星期
max_idx = np.argmax(steps)
min_idx = np.argmin(steps)
print(f'最多步數：{steps[max_idx]}({days[max_idx]})')
print(f'最少步數：{steps[min_idx]}({days[min_idx]})')
 
# 步數排序（橫列輸出）
idx = np.argsort(steps)
result = [f'{days[i]}:{steps[i]}' for i in idx]
print('步數排序：', result)