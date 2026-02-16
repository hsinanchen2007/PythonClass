# ch10_3.py, all() 和 any() 的應用
import numpy as np
# 每列代表不同時間點的溫度
temps = np.array([
    [25, 30],   # 時間點0，正常
    [15, 18],   # 時間點1，全部正常
    [12, 92]    # 時間點2，機台1過熱 (從0開始數)
]) 

# 檢查所有溫度是否正常
all_ok = np.all((temps >= 10) & (temps <= 90))
print('全部正常？', all_ok)
 
# 找出每個時間點是否有任何異常
has_problem = np.any((temps < 10) | (temps > 90), axis=1)
print('有異常時間點：', has_problem)