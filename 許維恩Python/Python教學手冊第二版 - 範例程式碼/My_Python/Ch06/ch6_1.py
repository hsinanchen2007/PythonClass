# ch6_1.py, 包含學生姓名及多科成績的巢狀串列
students = [
    ['Alice', [85, 90, 78]],  
    ['Bob', [88, 76, 92]],  
    ['Charlie', [90, 85, 89]]  
]

# 計算每位學生的平均成績
for student in students:
    name = student[0]
    scores = student[1]
    avg_score = sum(scores) / len(scores)
    print(f'{name} 的平均成績為 {avg_score:.2f}')  