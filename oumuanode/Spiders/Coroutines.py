import asyncio
import time


async def func1():
    print("你好呀")
    await asyncio.sleep(3)
    print("到付件")


async def func2():
    print("阿萨德刚")
    await asyncio.sleep(2)
    print("时间段")


async def func3():
    print("额吉")
    await asyncio.sleep(4)
    print("实际发货")


async def main():
    tasks = [
        asyncio.create_task(func1()),
        asyncio.create_task(func2()),
        asyncio.create_task(func3())
    ]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()
    print(t2 - t1)
