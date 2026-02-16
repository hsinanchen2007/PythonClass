# ex9_8.py
import numpy as np
a = np.array([[0, 1, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15]])
print("原始陣列 a：\n", a)

# (a) 不重複隨機挑選8個數字
print("\n(a) 從 a 中隨機挑選 8 個數字（不重複）：")
sample_a = np.random.choice(a.flatten(), size=8, replace=False)
print(sample_a)

# (b) 可重複隨機挑選10個數字
print("\n(b) 從 a 中隨機挑選 10 個數字（可重複）：")
sample_b = np.random.choice(a.flatten(), size=10, replace=True)
print(sample_b)

# (c) 隨機挑出 2 個不重複的橫列
print("\n(c) 從 a 中隨機挑出 2 個不重複的橫列：")
sample_c = a[np.random.choice(a.shape[0], size=2, replace=False)]
print(sample_c)

# (d) 將直行（欄）隨機排列
print("\n(d) 將 a 的直行隨機排列：")
shuffled_d = a[:, np.random.permutation(a.shape[1])]
print(shuffled_d)

'''output------------------------------
原始陣列 a：
 [[ 0  1  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]]

(a) 從 a 中隨機挑選 8 個數字（不重複）：        
[ 9 15 10  1  3  4 11  0]

(b) 從 a 中隨機挑選 10 個數字（可重複）：       
[6 1 8 8 6 5 7 6 0 4]

(c) 從 a 中隨機挑出 2 個不重複的橫列：
[[ 6  7  8  9 10]
 [11 12 13 14 15]]

(d) 將 a 的直行隨機排列：
[[ 4  3  1  0  5]
 [ 9  8  7  6 10]
 [14 13 12 11 15]]
------------------------------------'''