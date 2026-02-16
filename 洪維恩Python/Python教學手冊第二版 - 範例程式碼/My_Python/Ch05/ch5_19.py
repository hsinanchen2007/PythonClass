# ch5_19.py, 使用解包傳遞學生資料
def student_info(name, score):
    print(f'學生姓名: {name:<6} 成績: {score}')

# 學生資料，每個元素是一個包含姓名和成績的串列
students = [['John',  85], ['Alice', 92], ['Bob',   78]]
for student in students:  # 走訪學生資料並解包傳遞給函數
    student_info(*student)