# ch3_7.py, 處理手機號碼的分割、隱藏與格式化
phone = input('輸入手機號碼(格式：0912-345-678)：')
parts = phone.split('-')  		# 使用 split() 分割字串
formatted = ''.join(parts) 	# 使用 join() 去除 '-'
masked = f'{parts[0]}-***-{parts[-1]}' # 隱藏中間的部分
masked_f = formatted[:4]+'***'+formatted[-3:]  # 另一種隱藏格式

# 輸出結果
print(f'去除 – 後的號碼：{formatted}')
print(f'隱藏中間部分並用 - 隔開： {masked}')
print(f'隱藏中間部分： {masked_f}')