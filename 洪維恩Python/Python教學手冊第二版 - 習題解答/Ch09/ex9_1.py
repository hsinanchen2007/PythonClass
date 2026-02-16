# ex9_1.py
import numpy as np

# (a)
a = np.array([[2.5], [3.8], [7.1], [9.6]])
print('(a) a=\n', a)
print("a.shape =", a.shape)
print("a.ndim =", a.ndim)
print("a.size =", a.size)

# (b)
a = np.array([[2.5, 3.8, 7.1, 9.6]])
print('\n(b) a=', a)
print("a.shape =", a.shape)
print("a.ndim =", a.ndim)
print("a.size =", a.size)

# (c)
a = np.array([[12]])
print('\n(c) a=', a)
print("a.shape =", a.shape)
print("a.ndim =", a.ndim)
print("a.size =", a.size)

# (d)
a = np.array([
    [6, 6, 6, 6],
    [3, 3, 3, 3],
    [9, 9, 9, 9]
])
print('\n(d) a=\n', a)


'''output------------------------------
(a) a=
 [[2.5]
 [3.8]
 [7.1]
 [9.6]]
a.shape = (4, 1)
a.ndim = 2
a.size = 4

(b) a= [[2.5 3.8 7.1 9.6]]
a.shape = (1, 4)
a.ndim = 2
a.size = 4

(c) a= [[12]]
a.shape = (1, 1)
a.ndim = 2
a.size = 1

(d) a=
 [[6 6 6 6]
 [3 3 3 3]
 [9 9 9 9]]
------------------------------------'''