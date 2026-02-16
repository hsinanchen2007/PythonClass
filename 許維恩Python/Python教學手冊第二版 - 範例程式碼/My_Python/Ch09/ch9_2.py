# ch9_2.py, 使用 choice() 抽查學生成績
import numpy as np
rg = np.random.default_rng()   # 建立隨機數生成器
data = np.array([    # 建立二維陣列，包含學生姓名和單科成績
    ['Alice', 85],
    ['Bob', 92],
    ['Cathy', 78],
    ['David', 90],
])
# 從學生資料中隨機抽查 2 位學生的成績，不重複抽樣 
result = rg.choice(data, size=2, replace=False, axis=0) 
print(result)