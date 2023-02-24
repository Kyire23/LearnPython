import math
def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True
def primes(m, n):
    """返回[m, n]之间所有素数的生成器"""
    for i in range(m, n+1):
        if is_prime(i):
            yield i
#测试代码
if __name__ == '__main__':
    pimes1 = primes(5000000000, 5000000090)
    #pimes1 = primes(1, 100)
    for p in pimes1:
        print(p, end=',')
