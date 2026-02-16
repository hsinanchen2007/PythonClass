# ch14_10.py, 避免像素的溢位 
import matplotlib.pyplot as plt
from skimage import data

coins0 = data.coins()				# coins0的型別為uint8
coins1 = coins0.copy()			# coins1的型別為uint8
coins1 += 60  					# 將像素值都加60（溢位發生）

coins2 = coins0.copy().astype(int)	# coins1的型別為int
coins2 += 60  					# 將像素值都加60（不會溢位）
coins2[coins2 > 255] = 255			# 將大於255的像素值設為255

fig, ax = plt.subplots(1, 3, figsize=(10, 3))
ax[0].imshow(coins0, cmap='gray') 		# 原圖
ax[0].set_title('Original image') 	
ax[1].imshow(coins1, cmap='gray')		# 溢位發生
ax[1].set_title('Overflow occurs')	
ax[2].imshow(coins2, cmap='gray')		# 不會溢位
ax[2].set_title('Overflow prevented') 
plt.show()