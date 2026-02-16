# ch5_8.py, 傳遞可變物件到函數
def modify_list(lst):
    print('函數內部，lst 的位址:', id(lst))
    lst.append(100)	# 修改可變物件的內容
 
nums = [1, 2, 3]		# 建立一個串列(可變物件)
print('函數外部，nums 的位址:', id(nums))
 
modify_list(nums)   	# 呼叫函數，傳入可變物件
print('函數外部，nums 的內容:', nums)   # 檢查nums是否受到影響