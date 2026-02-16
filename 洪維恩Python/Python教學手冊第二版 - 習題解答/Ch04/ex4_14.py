# ex4_14.py
current_year = 2025  # 設定今年的年份
leap_years_count = 0

# 遍歷從 1 年到今年的每一年
for year in range(1, current_year + 1):
    # 判斷閏年的條件
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        leap_years_count += 1

print(f"從西元0001年到今年，共有 {leap_years_count} 個閏年")

'''output-------------------------
從西元0001年到今年，共有 491 個閏年
-------------------------------'''