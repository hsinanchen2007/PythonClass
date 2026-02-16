# ch4_3.py, 傳統與單行if-else 敘述的比較（判別成績是否及格）
score = int(input('請輸入分數：'))

if score >= 60: 			# 傳統的 if-else
    result1 = '及格'
else:
    result1 = '不及格'

result2 = '及格' if score >= 60 else '不及格'  # 單行的 if-else

print(f'傳統 if-else 的結果：{result1}')
print(f'單行 if-else 的結果：{result2}')