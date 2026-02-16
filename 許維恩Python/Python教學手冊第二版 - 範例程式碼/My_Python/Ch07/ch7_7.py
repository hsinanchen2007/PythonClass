# ch7_7.py, 使用靜態函數和類別函數來找尋質數
class PrimeChecker:
    @staticmethod		
    def is_prime(n): 		# 靜態函數，判別n是否為質數
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    @classmethod			# 類別函數，傳回小於limit的所有質數
    def find_primes(cls, limit):
        primes = [n for n in range(2, limit + 1) if cls.is_prime(n)]
        return primes

limit = 20
primes = PrimeChecker.find_primes(limit)
print(f'小於等於 {limit} 的質數有: {primes}')
print(PrimeChecker.is_prime(23))