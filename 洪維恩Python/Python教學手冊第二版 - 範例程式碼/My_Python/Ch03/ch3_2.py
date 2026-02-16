# ch3_2.py, random 模組模擬抽獎活動
import random
# 參加者名單，由學生名字組成的串列
students= ['Alice', 'Bob', 'Tom', 'David', 'Eve']  

# 隨機抽取兩位得獎者（不重複）
winners = random.sample(students, 2)

print('得獎者是：', winners)     # 輸出得獎者名單