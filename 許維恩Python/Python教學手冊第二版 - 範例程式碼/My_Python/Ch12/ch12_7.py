# ch12_7.py, 計算各科成績的平均值
import pandas as pd 
import numpy as np 
data = {'Math':[98, 96, 39],
         'Biology':[78, 89, 45],
         'English':[87, 98, 66]}

d0=pd.DataFrame(data,index=['Tom', 'Leo', 'Ava'])
print(d0)  							# 顯示所有學生的各科成績

mat_avg = round(np.mean(d0['Math']), 2)     		# 計算數學平均
bio_avg = round(np.mean(d0['Biology']), 2)  	# 計算生物平均
eng_avg = round(np.mean(d0['English']), 2)  	# 計算英文平均
# 印出每科的平均值
print(f'平均 {mat_avg:6.1f}{bio_avg:9.1f}{eng_avg:9.1f}')