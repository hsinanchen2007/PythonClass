# ex5_4.py
def primes(x):
    prime_list = []
    for n in range(2, x + 1):
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(n)
    return prime_list

x=20
print('小於等於',x,'的所有質數:',primes(x))

'''output---------------------------------------------
小於等於 20 的所有質數: [2, 3, 5, 7, 11, 13, 17, 19]
---------------------------------------------------'''