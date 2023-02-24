from threading import Thread


# 多线程
#
# def func():
#     for i in range(1000):
#         print("func", i)
#
#
# if __name__ == '__main__':
#     t = Thread(target=func())
#     t.start()  # 具体执行时间由cpu决定
#     for i in range(1000):
#         print("main", i)
# 第二种写法
class MyThread(Thread):
    def run(self):
        for i in range(100):
            print("子线程", i)


if __name__ == '__main__':
    t = MyThread()
    t.start()

    for i in range(100):
        print("主线程", i)

