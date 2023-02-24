from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


# 多进程
# def func():
#     for i in range(100):
#         print("子进程", i)
#
#
# if __name__ == '__main__':
#     p = Process(target=func)
#     p.start()
#     for i in range(100):
#         print("主进程", i)

# 线程池:一次开辟一些线程，我们用户直接给线程池提交任务，线程任务的调度交给线程池来完成

def fn(name):
    for i in range(100):
        print(name, i)


if __name__ == '__main__':
    with ThreadPoolExecutor(50) as t:
        for i in range(100):
            t.submit(fn, name=f"线程{i}")
    # 等待线程池中的任务全部执行完毕，才继续执行(守护）
    print("123")
