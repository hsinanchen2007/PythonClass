# ch7_12.py, 類別封裝的範例，保護銀行的帳戶資料
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance	# 私有屬性
    def get_balance(self):  		# 公有函數，用於獲取帳戶餘額
        return self.__balance
    def deposit(self, amount):  	# 公有函數，用於存款
            self.__balance += amount
            print(f'存入 {amount} 元，餘額 {self.get_balance()} 元')
    def withdraw(self, amount):  	# 公有函數，用於取款
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f'取出 {amount} 元，餘額 {self.get_balance()} 元')
        else:
            print('餘額不足')

acc = BankAccount(1000)
print(f'帳戶餘額: {acc.get_balance()} 元')
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(2000)  		# 取款金額無效或餘額不足
# print(acc.__balance)	# 錯誤，無法讀取私有屬性