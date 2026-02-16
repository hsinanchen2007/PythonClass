# ex6_15.py
def unique_intersection(set1, set2):
    # 使用集合的交集運算符 "&" 或迴圈來查找交集
    result = {elem for elem in set1 if elem in set2}
    return result

# 測試範例
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection = unique_intersection(set1, set2)
print(intersection)  # 輸出應為 {3, 4}

'''output-----
{3, 4}
-----------'''