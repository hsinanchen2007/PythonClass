# ch12_1.py, 計算成績平均
import pandas as pd  
scores = pd.Series({'Math':80, 'English':63, 'Biology':92})
total_score = 0                         		# 總分

for subject, score in scores.items():
    total_score += score                		# 計算加總
    print(f"{subject}: {score}")       		# 印出科目和分數
average_score = total_score / scores.size 	# 計算平均分數
print(f'平均: {average_score:.2f}')         	# 印出結果