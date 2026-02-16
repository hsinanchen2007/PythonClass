# ex4_32.py
nums = [8, 11, 98, 23, 47]
found = False
for num in nums:
    if num % 3 == 0:
        print(f"{num} 是可被3整除的數")
        found = True
if not found:
    print("沒有包含可被3整除的數")

'''output--------------------
沒有包含可被3整除的數
--------------------------'''