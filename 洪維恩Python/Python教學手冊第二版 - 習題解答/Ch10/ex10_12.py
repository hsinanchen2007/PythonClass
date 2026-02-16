# ex10_12.py
import numpy as np

points = np.array([
    [6, 4],
    [7, 1],
    [7, 4],
    [3, 8],
    [6, 9]
])

distances = np.sqrt(points[:, 0]**2 + points[:, 1]**2)
sorted_indices = np.argsort(distances)
sorted_points = points[sorted_indices]
sorted_distances = distances[sorted_indices]

print("依距離排序的點與其對應距離：")
for pt, d in zip(sorted_points, sorted_distances):
    x, y = int(pt[0]), int(pt[1])
    print(f"點 ({x}, {y})，距離原點 = {d:.2f}")

'''output--------------------
依距離排序的點與其對應距離：
點 (7, 1)，距離原點 = 7.07
點 (6, 4)，距離原點 = 7.21
點 (7, 4)，距離原點 = 8.06
點 (3, 8)，距離原點 = 8.54
點 (6, 9)，距離原點 = 10.82
--------------------------'''