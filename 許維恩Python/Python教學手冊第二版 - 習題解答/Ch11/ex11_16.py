# ex11_16.py
import numpy as np
import matplotlib.pyplot as plt

# 模擬擲骰子 10000 次
num_trials = 10000
dice_rolls = np.random.randint(1, 7, num_trials)

# 統計每個點數出現的次數（點數為 1~6）
counts = np.bincount(dice_rolls)[1:]

# 點數標籤
labels = np.arange(1, 7)

# 繪製長條圖
bars = plt.bar(labels, counts, color='skyblue', edgecolor='black')

# 在每個長條內部顯示數字（靠上，白色字）
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height * 0.85,  # 放在長條內部的85%高度
             str(height), ha='center', va='top', fontsize=10, color='white')

# 圖表標題與軸標籤
plt.xlabel('Dice Number')
plt.ylabel('Frequency')
plt.title('Distribution of Dice Rolls (10,000 trials)')

plt.show()

'''output-----

-----------'''