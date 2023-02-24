"""
@Author = oumuamuanode
@Time : 2022/10/16 14:54
"""
# d = {'x': 1, 'y': 2, 'z': 3}
# for key in d:
#  print(key, 'corresponds to', d[key])
#
# for key, value in d.items():
#  print(key, 'corresponds to', value)


# names = ['anne', 'beth', 'george', 'damon']
# ages = [12, 45, 32, 102]
# for i in range(len(names)):
#     print(names[i],'is',ages[i],'years old')
#
# print(list(zip(names,ages)))

# for name,age in zip(names,ages):
#     print(name,'is',age,'years old')

# index = 0
# for string in strings:
#  if 'xxx' in string:
#  strings[index] = '[censored]'
# index += 1

# for index, string in enumerate(strings):
#  if 'xxx' in string:
#  strings[index] = '[censored]'
# strings = ['anne', 'beth', 'george', 'damon']
# for index, string in enumerate(strings):
#     if 'beth' in string:
#         print(index,string)

# 反向迭代和排序后再迭代
# >>> sorted([4, 3, 6, 8, 3])
# [3, 3, 4, 6, 8]
# >>> sorted('Hello, world!')
# [' ', '!', ',', 'H', 'd', 'e', 'l', 'l', 'l', 'o', 'o', 'r', 'w']
# >>> list(reversed('Hello, world!'))
# ['!', 'd', 'l', 'r', 'o', 'w', ' ', ',', 'o', 'l', 'l', 'e', 'H']
# >>> ''.join(reversed('Hello, world!'))
# '!dlrow ,olleH'

# from math import sqrt
#
# for n in range(99, 0, -1):
#     root = sqrt(n)
#     if root == int(root):
#         print(n)
#         break

# range(0, 10, 2)
# word = 'dummy'
# while word:
#     word = input('Please enter a word: ')
#     # 使用这个单词做些事情：
#     print('The word was', word)

# while True:
#     word = input('Please enter a word: ')
#     if not word: break
#     # 使用这个单词做些事情：
#     print('The word was ', word)

# from math import sqrt
#
# for n in range(99, 81, -1):
#     root = sqrt(n)
#     if root == int(root):
#         print(n)
#         break
# else:
#     print("Didn't find it!")

d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
print(d.items())