# ch12_5.py, 動物醫療資料的索引與分組
import pandas as pd
# 建立動物醫療資料
data={'Species': ['Cat', 'Dog', 'Dog', 'Rabbit', 'Turtle'],
      'Weight': [4.2, 9.1, 7.8, 1.3, 2.4],
      'Health': ['良好', '中等', '良好', '差', '良好']}
index=['小花', '阿毛', '阿呆', '球球', '小龜']
df = pd.DataFrame(data, index=index)

# 重新指定索引順序
new_order = ['阿呆', '小花', '球球', '阿毛', '小龜']
df_reindex = df.reindex(new_order)
print("重新指定索引順序後的資料：")
print(df_reindex)

# 依健康狀況分組
group = df.groupby('Health', as_index=False)
print("\n依健康狀況分組後的資料：")
for health, group_data in group:
    print(f"健康狀況: {health}")
    print(group_data)