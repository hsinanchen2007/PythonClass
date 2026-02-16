# ex10_15.py
import numpy as np

# (a)
a1 = np.array([[1, 2], [1, 2], [1, 3]])
b1 = np.array([0, 1, 3])
x1, residuals1, rank1, s1 = np.linalg.lstsq(a1, b1, rcond=None)
print("(a) 最小平方解：", x1)
print("    殘差：", residuals1)

# (b)
a2 = np.array([[2, 1], [1, 2], [1, 1]])
b2 = np.array([2, 0, -3])
x2, residuals2, rank2, s2 = np.linalg.lstsq(a2, b2, rcond=None)
print("(b) 最小平方解：", x2)
print("    殘差：", residuals2)

'''output----------------------------
(a) 最小平方解： [-4.5  2.5]
    殘差： [0.5]
(b) 最小平方解： [ 1. -1.]
    殘差： [11.]
----------------------------------'''