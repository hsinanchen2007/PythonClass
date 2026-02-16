# ex5_17.py
def find_max(*numbers):
    return max(numbers) if numbers else None

# 測試
print('find_max(4, 9, 3)=',find_max(4, 9, 3))
print('find_max(6, 4)=',find_max(6, 4))
print('find_max()=',find_max())

'''output-----------------------------------
find_max(4, 9, 3)= 9
find_max(6, 4)= 6
find_max()= None
-----------------------------------------'''