# ex10_20.py
import numpy as np
# (a) 將陣列 a 轉成 bytes 物件，並將結果設定給變數 z
a = np.array([1, 4, 5, 7, 8])
z = a.tobytes()
print("(a) 使用 tobytes() 轉換的 bytes 物件：")
print(z)

# (b) 使用 frombuffer() 讀取 z 並驗證是否與 a 相同
a_from_z = np.frombuffer(z, dtype=a.dtype)
print("\n(b) 從 bytes 物件讀取的陣列：")
print(a_from_z)
# 驗證結果是否相同
print("是否相同：", np.array_equal(a, a_from_z))

# (c) 將陣列 a 儲存為 .npy 檔案並重新讀取
np.save("Ch10/example", a)
# 從檔案讀取回來
a_loaded = np.load("Ch10/example.npy")
print("\n(c) 從 example.npy 讀取的陣列：")
print(a_loaded)
# 驗證是否相同
print("是否相同：", np.array_equal(a, a_loaded))

'''output-------------------------------------------------------------------------------------------------------------------------------------------------------------
(a) 使用 tobytes() 轉換的 bytes 物件：
b'\x01\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00'

(b) 從 bytes 物件讀取的陣列：
[1 4 5 7 8]
是否相同： True

(c) 從 example.npy 讀取的陣列：
[1 4 5 7 8]
是否相同： True
-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''