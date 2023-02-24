import time
def timing(f, data):
    """测量函数调用f(data)的运行时间分析"""
    start = time.time() #记录开始时间
    f(data)             #运行f(data)
    end = time.time()   #记录结束时间
    return end - start  #返回执行时间

#测试代码
if __name__ == "__main__":
    import pi #参见14.7.2
    for i in range(3):
        n = 10000*(100**i)
        t = timing(pi.pi, n)
        print("pi({})的运行时间为：{}".format(n, t))

