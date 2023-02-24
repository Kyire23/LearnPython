"""
@Author = oumuamuanode
@Time : 2022/10/16 13:36
"""
# months = [
#  'January',
#  'February',
#  'March',
#  'April',
#  'May',
#  'June',
#  'July',
#  'August',
#  'September',
#  'October',
#  'November',
#  'December'
# ]
# # 一个列表，其中包含数1～31对应的结尾
# endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
#  + ['st', 'nd', 'rd'] + 7 * ['th'] \
#  + ['st']
# year = input('Year: ')
# month = input('Month (1-12): ')
# day = input('Day (1-31): ')
#
# month_number = int(month)
# day_number = int(day)
#
# # 别忘了将表示月和日的数减1，这样才能得到正确的索引
# month_name = months[month_number-1]
# ordinal = day + endings[day_number-1]
#
# print(month_name + ' ' + ordinal + ', ' + year)

# 从类似于http://www.something.com的URL中提取域名
# url = input('Please enter the URL:')
# domain = url[11:-4]
# print("Domain name: " + domain)

# 在位于屏幕中央且宽度合适的方框内打印一个句子
# 在位于屏幕中央且宽度合适的方框内打印一个句子
# sentence = input("Sentence: ")
# screen_width = 80
# text_width = len(sentence)
# box_width = text_width + 6
# left_margin = (screen_width - box_width) // 2
# print()
# print(' ' * left_margin + '+' + '-' * (box_width-2) + '+')
# print(' ' * left_margin + '| ' + ' ' * text_width + ' |')
# print(' ' * left_margin + '| ' + sentence + ' |')
# print(' ' * left_margin + '| ' + ' ' * text_width + ' |')
# print(' ' * left_margin + '+' + '-' * (box_width-2) + '+')
# print()

# 检查用户名和PIN码
# database = [
#  ['albert', '1234'],
#  ['dilbert', '4242'],
#  ['smith', '7524'],
#  ['jones', '9843']
# ]
# username = input('User name: ')
# pin = input('PIN code: ')
# if [username, pin] in database: print('Access granted')

# name = list('Perl')
# name[2:] = list('ar')
# name[1:] = list('ython')
# print(name)

a = [1, 2, 3]
b = [4, 5, 6]
# a.extend(b)
a[len(a):] = b
# 可读性不高
print(a)


# x = [4, 6, 2, 1, 7, 9]
# print(x)
# x.sort(reverse=False)
# print(x)
# x.sort(reverse=True)
# print(x)

# 元组 逗号至关重要，不能修改 仅将值用圆括号括起不管用：(42)与42完全等效。但仅仅加上一个逗号，就能完全改变表达式的值。
# >>> 3 * (40 + 2)
# 126
# >>> 3 * (40 + 2,)
# (42, 42, 42)

# """
# 序列是一种数据结构，其中的元素带编号（编号从0开 始 ）。 列 表 、 字 符 串 和 元 组
# 都属于序列，其中列表是可变的（你可修改其内容），而元组和字符串是不可变的（一旦
# 创建，内容就是固定的）。要访问序列的一部分，可使用切片操作：提供两个指定切片起
# 始和结束位置的索引。要修改列表，可给其元素赋值，也可使用赋值语句给切片赋值。
# """
#
# print( "{}, {} and {}".format("first", "second", "third") )
# print("{3} {0} {2} {1} {3} {0}".format("be", "not", "or", "to") )
# print("{foo} {} {bar} {}".format(1, 2, bar=4, foo=3))