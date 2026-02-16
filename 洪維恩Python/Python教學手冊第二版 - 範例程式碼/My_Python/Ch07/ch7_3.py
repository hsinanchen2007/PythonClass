# ch7_3.py, 悠遊卡的儲值與消費
class EasyCard:
   def __init__(self, owner, amount=0):
      self.name = owner			# 持有者姓名
      self.balance = amount  		# 帳戶餘額
      print( f'{self.name} 新卡儲值 {amount}')
   def add_value(self, amount):	# 儲值（實例函數）
      self.balance += amount
      print( f'{self.name} 儲值 {amount}，餘額：{self.balance}')
   def spend(self, amount):		# 消費（實例函數）
      if amount <= self.balance:	# 消費金額小於餘額
         self.balance -= amount
         print(f'{self.name} 消費 {amount}，餘額：{self.balance}')
      else:
         print('餘額不足')

ac1 = EasyCard('Mary',50)		# 建立EasyCard類別的物件，並儲值50
ac1.add_value(300)			# 儲值300
ac1.spend(200)				# 消費200
ac1.spend(400)				# 嘗試消費400，但餘額不足
ac2 = EasyCard('Tom', 100) 	# 建立EasyCard類別的物件，並儲值100
ac2.spend(20)					# 消費20