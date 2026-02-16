# ex5_31.py
# (a) 定義函數fib(n)，傳回前n個費式數列的值
def fib(n):
    fib_sequence = [1, 1]  # 初始的費式數列前兩項
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence[:n]

# (b) 定義費式數列產生器fib_gen(n)
def fib_gen(n):
    a, b = 1, 1
    yield a
    yield b
    for _ in range(2, n):
        a, b = b, a + b
        yield b

# 顯示結果
n=10
print(f"(a) 使用函數fib({n}) 計算前{n}項費式數列:")
print(fib(n))  # 使用函數顯示前 n 項費式數列
print(f"\n(b) 使用產生器fib_gen({n}) 計算前{n}項費式數列:")
print(list(fib_gen(n)))  # 使用產生器顯示前 n 項費式數列

'''output----------------------------------
(a) 使用函數fib(10) 計算前10項費式數列:
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

(b) 使用產生器fib_gen(10) 計算前10項費式數列:
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
----------------------------------------'''