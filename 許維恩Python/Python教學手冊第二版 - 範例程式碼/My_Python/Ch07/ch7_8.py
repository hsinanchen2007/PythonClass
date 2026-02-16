# ch7_8.py, 簡單的繼承範例
class Animal:  				# 父類別
    def speak(self):  			# 父類別裡的speak()
        print('動物發出聲音')  
    def run(self):    			# 父類別裡的run()
        print('動物在奔跑')  

class Dog(Animal):  		# 子類別Dog繼承自父類別Animal  
    def speak(self):  		# 子類別自己的speak()
        print('汪汪！')  
        super().speak()  	# 呼叫父類別的speak()  

dog = Dog() 		# 建立子類別的物件
dog.speak()  		# 呼叫自己的speak()函數
dog.run()   		# 直接呼叫由父類別繼承過來的函數