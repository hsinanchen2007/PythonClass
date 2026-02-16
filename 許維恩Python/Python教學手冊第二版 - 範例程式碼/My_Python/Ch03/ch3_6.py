# ch3_6.py, 使用wcswidth() 對齊文字
from wcwidth import wcswidth     # 載入wcswidth函數
 
print('使用ljust() 對齊文字:')
print('蘋果(Apple)'.ljust(14) + '20元')
print('奇異果(Kiwi)'.ljust(14) + '40元')
print('梅(Plum)'.ljust(14) + '50元')

print('使用 wcswidth() 對齊文字:')
print('蘋果(Apple)' + ' '*(14-wcswidth('蘋果(Apple)')) + '20元')
print('奇異果(Kiwi)' + ' '*(14-wcswidth('奇異果(Kiwi)')) + '40元')
print('梅(Plum)' + ' '*(14-wcswidth('梅(Plum)')) + '50元')