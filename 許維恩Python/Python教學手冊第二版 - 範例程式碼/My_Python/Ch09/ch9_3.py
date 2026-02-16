# ch9_3.py, 陣列提取的應用
import numpy as np
scores = np.array([		# 每行分別是國文、英文、數學和自然成績
    [72, 88, 91, 65],		# Tom
    [85, 67, 78, 90],		# Jerry
    [60, 75, 80, 70]		# Mary
])
names = np.array(['Tom', 'Jerry', 'Mary'])
 
print('Jerry的數學成績:', scores[1, 2])  # 索引
print('Tom和Jerry的國文、英文成績:\n', scores[0:2, 0:2])  # 切片
 
print('Tom和Mary的自然成績:', scores[[0, 2],[3, 3]])     # 花式
 
# 布林陣列：找出數學成績大於 80 的學生
mask = scores[:, 2] > 80		# mask的值為 [True False False]
print('Math > 80:', names[mask])