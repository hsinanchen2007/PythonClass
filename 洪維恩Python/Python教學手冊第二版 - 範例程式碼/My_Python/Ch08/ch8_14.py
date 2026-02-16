# ch8_14.py, 自定義模組的載入練習
import sys
# 將自定義模組的路徑加入系統模組搜尋路徑
sys.path.append('C:\\python\\my_code')  

from greeting import say_hello	# 從greeting載入say_hello()
say_hello('Jeanne')	# 呼叫say_hello()

from math_code import calculator	# 從math_code載入calculator模組
print(calculator.add(6,4))	# 呼叫add() 進行加法運算

import geometry.area as ar  	# 載入模組並命名為ar
print(ar.circle(2))    	# 呼叫circle()

from geometry.area import circle	# 直接載入 circle() 函數
print(circle(10))	# 呼叫circle()