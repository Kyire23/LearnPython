"""
@Author = oumuamuanode
@Time : 2022/10/16 14:31
"""
# 一个简单的数据库
# 一个将人名用作键的字典。每个人都用一个字典表示，
# 字典包含键'phone'和'addr'，它们分别与电话号码和地址相关联
# people = {
#     'Alice': {
#         'phone': '2341',
#         'addr': 'Foo drive 23'
#     },
#     'Beth': {
#         'phone': '9102',
#         'addr': 'Bar street 42'
#     },
#     'Cecil': {
#         'phone': '3158',
#         'addr': 'Baz avenue 90'
#     }
# }
# 电话号码和地址的描述性标签，供打印输出时使用
# labels = {
#     'phone': 'phone number',
#     'addr': 'address'
# }
# name = input('Name: ')
# # 要查找电话号码还是地址？
# request = input('Phone number (p) or address (a)? ')
# # 使用正确的键：
# if request == 'p': key = 'phone'
# if request == 'a': key = 'addr'
# # 仅当名字是字典包含的键时才打印信息：
# if name in people: print("{}'s {} is {}.".format(name, labels[key], people[name][key]))

# 一个使用get()的简单数据库
# 在这里插入代码清单4-1中的数据库（字典people）
# labels = {
#  'phone': 'phone number',
#  'addr': 'address'
# }
# name = input('Name: ')
# # 要查找电话号码还是地址？
# request = input('Phone number (p) or address (a)? ')
# # 使用正确的键：
# key = request # 如果request既不是'p'也不是'a'
# if request == 'p': key = 'phone'
# if request == 'a': key = 'addr'
# # 使用get提供默认值
# person = people.get(name, {})
# label = labels.get(key, key)
# result = person.get(key, 'not available')
# print("{}'s {} is {}.".format(name, label, result))
# names1=['Amy','Bob','Charlie','Daling']
# names2=names1; names3=names1[:]
# names2[0]='Alice';names3[1]='Ben'
# sum=0
# for ls in (names1,names2,names3):
#     if ls[0] == 'Alice':sum +=1
#     if ls[1] == 'Ben': sum+=2;
# print(sum)


# width = int(input('Please enter width: '))
# price_width = 10
# item_width = width - price_width
# header_fmt = '{{:{}}}{{:>{}}}'.format(item_width, price_width)
# fmt = '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)
# print('=' * width)
# print(header_fmt.format('Item', 'Price'))
# print('-' * width)
# print(fmt.format('Apples', 0.4))
# print(fmt.format('Pears', 0.5))
# print(fmt.format('Cantaloupes', 1.92))
# print(fmt.format('Dried Apricots (16 oz.)', 8))
# print(fmt.format('Prunes (4 lbs.)', 12))
# print('=' * width)


print("The Middle by Jimmy Eat World".center(39, "*"))
