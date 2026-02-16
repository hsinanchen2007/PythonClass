# ch7_1.py, 計算圓面積與周長（傳統的寫法）
def area(radius):				# 圓面積函數
    return 3.14 * radius ** 2
def perimeter(radius):		# 圓周長函數
    return 2 * 3.14 * radius

radius = 4    # 半徑
c_area = area(radius)   		# 計算圓面積
c_peri= perimeter(radius)		# 計算圓周長
print(f'半徑: {radius}, 面積: {c_area}, 周長: {c_peri}')