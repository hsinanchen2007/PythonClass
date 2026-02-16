# ch4_5.py, 成績等級評定
score = int(input('請輸入分數: '))  # 輸入分數，並轉換為整數

if score >= 90:		# 判斷分數是否大於等於90
    grade = 'A'		
elif score >= 80: 	# 如果小於90，且大於等於80
    grade = 'B' 
elif score >= 70: 	# 如果小於80，且大於等於70
    grade = 'C'  
elif score >= 60: 	# 如果小於70，且大於等於60
    grade = 'D' 
else:  				# 若以上條件皆不成立（小於60）
    grade = 'F'  		
print(f'你的等級是: {grade}')  #輸出成績等級