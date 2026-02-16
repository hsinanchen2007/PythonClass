# ex4_19.py
data = [[2, 4, 5], [5, 8, None], [10, 3, 4]]
for i, group in enumerate(data, 1):
    if None in group:
        print(f"第{i}組：Incomplete data")
    else:
        print(f"第{i}組：總和為{sum(group)}")

'''output--------------------
第1組：總和為11
第2組：Incomplete data
第3組：總和為17
--------------------------'''