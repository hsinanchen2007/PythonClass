# ex10_7.py
import numpy as np

a = np.array([
    [0, 1, 2, 3, 4],
    [2, 3, 4, 0, 1],
    [4, 0, 1, 2, 3],
    [1, 2, 3, 4, 0],
    [3, 4, 0, 1, 2]
])

# (a) 離 (2,2) 最近，值為 4 的座標
target = (2, 2)
positions = np.argwhere(a == 4)
distances = np.sum(np.abs(positions - target), axis=1)
closest_pos = positions[np.argmin(distances)]
print(f"(a) 離 (2,2) 最近，值為 4 的座標：({closest_pos[0]},{closest_pos[1]})")

# (b) 離 (4,3) 最近，值為 0 的座標
target = (4, 3)
positions = np.argwhere(a == 0)
distances = np.sum(np.abs(positions - target), axis=1)
closest_pos = positions[np.argmin(distances)]
print(f"(b) 離 (4,3) 最近，值為 0 的座標：({closest_pos[0]},{closest_pos[1]})")

# (c) 離 (4,0) 最近，值為 2 的座標
target = (4, 0)
positions = np.argwhere(a == 2)
distances = np.sum(np.abs(positions - target), axis=1)
closest_pos = positions[np.argmin(distances)]
print(f"(c) 離 (4,0) 最近，值為 2 的座標：({closest_pos[0]},{closest_pos[1]})")

# (d) 相距最遠的兩個值為 4 的座標
positions = np.argwhere(a == 4)
max_dist = 0
farthest_pair = None
for i in range(len(positions)):
    for j in range(i + 1, len(positions)):
        dist = np.sum(np.abs(positions[i] - positions[j]))
        if dist > max_dist:
            max_dist = dist
            farthest_pair = (positions[i], positions[j])
print(f"(d) 相距最遠的兩個值為 4 的座標：({farthest_pair[0][0]},{farthest_pair[0][1]}) 和 ({farthest_pair[1][0]},{farthest_pair[1][1]})")

# (e) 陣列中值為 0 的元素個數
count_zeros = np.sum(a == 0)
print(f"(e) 陣列中值為 0 的元素個數：{count_zeros}")

'''output------------------------------------------
(a) 離 (2,2) 最近，值為 4 的座標：(1,2)
(b) 離 (4,3) 最近，值為 0 的座標：(4,2)
(c) 離 (4,0) 最近，值為 2 的座標：(3,1)
(d) 相距最遠的兩個值為 4 的座標：(0,4) 和 (4,1)
(e) 陣列中值為 0 的元素個數：5
------------------------------------------------'''