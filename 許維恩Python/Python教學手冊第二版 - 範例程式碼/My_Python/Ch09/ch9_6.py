# ch9_6.py, 陣列的切割與重排
import numpy as np
mat = np.array([[4, 6, 1, 7, 4, 9],
                 [5, 0, 4, 2, 5, 8],
                 [0, 2, 1, 5, 7, 2],
                 [6, 8, 9, 3, 8, 6]])
 
# Step 1: 切成兩塊（2x6）
rows = np.vsplit(mat, 2)
 
# Step 2: 每塊切成三個 2x2
blocks = [np.hsplit(r, 3) for r in rows]

# Step 3: 每個 2x2 攤平成 1x4
flat = [b.reshape(1, 4) for grp in blocks for b in grp]

# Step 4: 垂直合併
out = np.concatenate(flat, axis=0)

print('重排後的新陣列:')
print(out)