# ex6_21.py
def make_dict(keys, values=None):
    if values is None:
        # 若沒有提供 values，則所有鍵對應的值為 0
        return {key: 0 for key in keys}
    else:
        # 若提供了 values，則將 keys 和 values 對應組成字典
        return dict(zip(keys, values))

# 測試範例
print('make_dict([0, 1, 2], [32, 43, 55]):', make_dict([0, 1, 2], [32, 43, 55]))
print('make_dict([0, 1, 2]):', make_dict([0, 1, 2]))

'''output---------------------------------------------------
make_dict([0, 1, 2], [32, 43, 55]): {0: 32, 1: 43, 2: 55}
make_dict([0, 1, 2]): {0: 0, 1: 0, 2: 0}
---------------------------------------------------------'''