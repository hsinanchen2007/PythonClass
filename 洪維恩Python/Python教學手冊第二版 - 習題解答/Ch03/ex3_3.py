# ex3_3.py
import math
result_a = math.sin(2.5) + math.exp(1.4)
result_b = math.ceil(6.3**2 - 0.5)
result_c = math.floor(math.cos(0.5**2) + math.sqrt(2))
result_d = math.gcd(math.gcd(6, 8), 12)
result_e = float('inf') - 2 * float('inf')
result_f = 3**0.5
result_g = math.log2(1024)
result_h = math.log(49**3, 7)
result_i = math.asin(-0.7) + math.atan(math.pi**2)

# 輸出結果
print(f"(a) sin(2.5) + e^1.4 = {result_a}")
print(f"(b) ⌈6.3^2 - 0.5⌉ = {result_b}")
print(f"(c) ⌊cos(0.5^2) + √2⌋ = {result_c}")
print(f"(d) 6, 8 和 12 的最大公因數 = {result_d}")
print(f"(e) ∞ - 2 × ∞ = {result_e}")
print(f"(f) 3^0.5 = {result_f}")
print(f"(g) log_2 1024 = {result_g}")
print(f"(h) log_7 (49^3) = {result_h}")
print(f"(i) sin^(-1)(-0.7) + tan^(-1)(π^2) = {result_i}")

'''output---------------------------------------------------
(a) sin(2.5) + e^1.4 = 4.653672110948631
(b) ⌈6.3^2 - 0.5⌉ = 40
(c) ⌊cos(0.5^2) + √2⌋ = 2
(d) 6, 8 和 12 的最大公因數 = 2
(e) ∞ - 2 × ∞ = nan
(f) 3^0.5 = 1.7320508075688772
(g) log_2 1024 = 10.0
(h) log_7 (49^3) = 6.0
(i) sin^(-1)(-0.7) + tan^(-1)(π^2) = 0.6944222469134894
---------------------------------------------------------'''