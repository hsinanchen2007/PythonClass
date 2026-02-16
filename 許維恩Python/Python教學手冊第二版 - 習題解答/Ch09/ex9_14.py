# ex9_14.py
import numpy as np
a = np.arange(12)
print('a=',a)
# (a) 查詢陣列 a 的 size、shape 和 ndim 屬性
print("(a)", "size:", a.size, ", shape:", a.shape, ", ndim:", a.ndim)

b = a.reshape(4, 3)
print("(b) 將a重塑為4×3的陣列\n", b)

c = a.reshape(1, 12)
print("\n將a重塑為1×12的陣列\n", c)

d = a.reshape(12, 1)
print("\n將a重塑為12×1的陣列\n", d)

e = a.reshape(2, 2, 3)
print("\n將a重塑為2×2×3的陣列\n", e)

'''output-----------------------------------
(a) size: 12 , shape: (12,) , ndim: 1
(b) 將a重塑為4×3的陣列
 [[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]

將a重塑為1×12的陣列
 [[ 0  1  2  3  4  5  6  7  8  9 10 11]]

將a重塑為12×1的陣列
 [[ 0]
 [ 1]
 [ 2]
 [ 3]
 [ 4]
 [ 5]
 [ 6]
 [ 7]
 [ 8]
 [ 9]
 [10]
 [11]]

將a重塑為2×2×3的陣列
 [[[ 0  1  2]
  [ 3  4  5]]

 [[ 6  7  8]
  [ 9 10 11]]]
-----------------------------------------'''