"""
@Author = oumuamuanode
@Time : 2022/10/16 15:17
"""


# fibs = [0, 1]
# for i in range(8):
#     fibs.append(fibs[-2] + fibs[-1])
# print(fibs)
#

# fibs = [0, 1]
# num = int(input('How many Fibonacci numbers do you want? '))
# for i in range(num - 2):
#     fibs.append(fibs[-2] + fibs[-1])
# print(fibs)

# def story(**kwds):
#     return 'Once upon a time, there was a ' \
#            '{job} called {name}.'.format_map(kwds)
#
#
# def power(x, y, *others):
#     if others:
#         print('Received redundant parameters:', others)
#     return pow(x, y)
#
#
# def interval(start, stop=None, step=1):
#     'Imitates range() for step > 0'
#     if stop is None:
#         start, stop = 0, start  # 就调整参数start和stop的值
#     result = []
#
#     i = start
#     # 从start开始往上数
#     while i < stop:
#         result.append(i)
#         i += step
#         return result
#
#
# print(story(job='king', name='Gumby'))
