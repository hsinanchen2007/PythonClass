# ex4_34.py
# (a) 建立一個 1 到 10 的平方所組成的串列
squares = [x**2 for x in range(1, 11)]
print("(a)", squares)

# (b) 建立一個 1 到 50 之間，可以同時被 3 和 4 整除的串列
divisible_by_3_and_4 = [x for x in range(1, 51) if x % 3 == 0 and x % 4 == 0]
print("(b)", divisible_by_3_and_4)

# (c) 取出字串 'List comprehension' 中所有的母音，並組成一個字元串列
vowels = [ch for ch in "List comprehension" if ch.lower() in "aeiou"]
print("(c)", vowels)

# (d) 依串列 [3, -1, 4, 7, -3, 2] 的值來建立另一個新串列
original_list = [3, -1, 4, 7, -3, 2]
transformed_list = [1 if x > 0 else -1 for x in original_list]
print("(d)", transformed_list)

'''output--------------------------------------
(a) [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
(b) [12, 24, 36, 48]
(c) ['i', 'o', 'e', 'e', 'i', 'o']
(d) [1, -1, 1, 1, -1, 1]
--------------------------------------------'''