# ch3_1.py, math 模組的使用範例
import math

# 計算圓的面積
radius = float(input('輸入圓的半徑：'))
area = math.pi * (radius ** 2)
print(f'圓的面積是：{area:.2f}')

# 計算平方根
num = abs(float(input('輸入一個數：')))      # 取絕對值，避免錯誤
sqrt_value = math.sqrt(num)
print(f'{num} 的平方根是：{sqrt_value:.2f}')

# 四捨五入的計算
float_num = float(input('輸入一個浮點數：'))
rounded_num = round(float_num)
print(f'{float_num} 捨入到整數的結果是：{rounded_num}')