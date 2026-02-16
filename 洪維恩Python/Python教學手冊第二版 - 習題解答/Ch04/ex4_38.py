# ex4_38.py
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 使用巢狀串列生成式將每個數字加1
new_matrix = [[element + 1 for element in row] for row in matrix]
print(new_matrix)

'''output----------------------------
[[2, 3, 4], [5, 6, 7], [8, 9, 10]]
----------------------------------'''