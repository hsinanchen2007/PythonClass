# ch4_26.py，字母與數字的組合
chars = ['a', 'b']
numbers = ['1', '2', '3']
combinations = [c + n for c in chars  for n in numbers]
print(combinations)