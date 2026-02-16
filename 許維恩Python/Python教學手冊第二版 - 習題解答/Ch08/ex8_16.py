# ex8_16.py, 主程式
import sys
sys.path.append('C:/python_pkg')  # 加入模組所在的資料夾路徑
from ex8_16_math1 import prime_factors
from ex8_16_math2 import prime_factors

# 計算 60 和 100 的質因數
factors_60 = prime_factors(60)
factors_100 = prime_factors(100)
print(f"60 的質因數: {factors_60}")
print(f"100 的質因數: {factors_100}\n")

# 計算 150 和 512 的質因數
factors_150 = prime_factors(150)
factors_512 = prime_factors(512)

print(f"150 的質因數: {factors_150}")
print(f"512 的質因數: {factors_512}")

'''output-----------------------------------
60 的質因數: [2, 2, 3, 5]
100 的質因數: [2, 2, 5, 5]

150 的質因數: [2, 3, 5, 5]
512 的質因數: [2, 2, 2, 2, 2, 2, 2, 2, 2]
-----------------------------------------'''