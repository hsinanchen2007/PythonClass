# ex7_12.py
class Factor:
    factor_list = [2, 3, 6, 8]  # 類別屬性，預設因數串列

    def __init__(self, num):
        print('初始的factor_list: ', Factor.factor_list)  # 輸出初始的factor_list
        self.num = num  # 實例屬性 num

    def find_factors(self):
        # 回傳能夠整除 num 的因數列表
        return [f for f in Factor.factor_list if self.num % f == 0]

    @classmethod
    def add_factors(cls, lst):
        # 將 lst 中不在 factor_list 的元素加入
        for element in lst:
            if element not in cls.factor_list:
                cls.factor_list.append(element)

    @classmethod
    def remove_factors(cls, lst):
        # 移除 factor_list 中出現於 lst 的元素
        for element in lst:
            if element in cls.factor_list:
                cls.factor_list.remove(element)

    @classmethod
    def show_factor_list(cls):
        # 顯示目前的 factor_list
        print(cls.factor_list)

    @staticmethod
    def isfactor(num, n):
        # 判斷 n 是否為 num 的因數
        return num % n == 0

# 測試
f0 = Factor(12)  # 輸出: 初始的factor_list: [2, 3, 6, 8]
print(f0.find_factors())  # 輸出: [2, 3, 6]
Factor.add_factors([4, 6, 9])
Factor.show_factor_list()  # 輸出: [2, 3, 6, 8, 4, 9]
Factor.remove_factors([3, 8])
Factor.show_factor_list()  # 輸出: [2, 6, 4, 9]
print(Factor.isfactor(15, 3))  # 輸出: True
print(Factor.isfactor(15, 4))  # 輸出: False

'''output------------------------------
初始的factor_list:  [2, 3, 6, 8]
[2, 3, 6]
[2, 3, 6, 8, 4, 9]
[2, 6, 4, 9]
True
False
------------------------------------'''