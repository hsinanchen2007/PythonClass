# ch12_4.py, 動物資料篩選
import pandas as pd
data={'Weight': [4.5, 8.0, 1.2, 2.3, 0.3],
      'Species': ['Cat', 'Dog', 'Rabbit', 'Turtle', 'Bird'],
      'Adopted': [False, True, False, False, True]}

names = ['Tom', 'Max', 'Leo', 'Sam', 'Ben']
df = pd.DataFrame(data, index=names)    # 建立DataFrame

print('動物資料:\n', df)
# 篩選體重小於2公斤且未被領養的動物
result = df[(df['Weight'] < 2) & (df['Adopted'] == False)]
print('\n體重小於2公斤且未被領養的動物:\n', result)