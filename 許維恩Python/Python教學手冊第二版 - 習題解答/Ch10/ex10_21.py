# ex10_21.py
import numpy as np

# 定義陣列 a, b, c
a = np.array([[0, 2], [1, 6]])
b = np.array([7, 2, 1])
c = np.array([[0, 2, 0], [6, 4, 2], [8, 3, 4]])

# 使用 savez 儲存到 variables.npz
np.savez('Ch10/variables', ar=a, br=b, cr=c)

# 讀取 variables.npz 並提取出變數 ar, br, cr
loaded_data = np.load('Ch10/variables.npz')
ar = loaded_data['ar']
br = loaded_data['br']
cr = loaded_data['cr']

# 印出結果
print("ar:", ar)
print("\nbr:", br)
print("\ncr:", cr)

'''output---------------------------
ar: [[0 2]
 [1 6]]

br: [7 2 1]

cr: [[0 2 0]
 [6 4 2]
 [8 3 4]]
---------------------------------'''