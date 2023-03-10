import time
import concurrent.futures as cf
def gcd(pair):
    # 求最大公约数
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
if __name__ == '__main__':
    #测试数据
    TEST_DATA = [(11880774, 83664910), (13961044, 17644234), (10112000, 13380625)]
    #传统串行方法
    start_time = time.time()
    res1 = list(map(gcd, TEST_DATA))
    end_time = time.time()
    print("串行处理结果：{}，消耗时间：{}".format(res1, end_time - start_time))
    #使用ProcessPoolExecutor并行处理
    start_time = time.time()
    pool = cf.ProcessPoolExecutor(max_workers=4)
    res2 = list(pool.map(gcd, TEST_DATA))
    end_time = time.time()
    print("并行处理结果：{}，消耗时间：{}".format(res2, end_time - start_time))
