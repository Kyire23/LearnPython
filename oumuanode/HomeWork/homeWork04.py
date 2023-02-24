# 1.插入数据到列表
#
# s = [1, 4, 6, 9, 13, 16, 19, 28, 40, 100]
# print("原始列表", s)
# nums1 = []
# count = 0
# a = int(input("插入一个数字:"))
#
# for i in range(len(s) - 1):
#     for j in range(len(s) - i - 1):
#         if s[j] > s[j + 1]:
#             count = s[j]
#             s[j] = s[j + 1]
#             s[j + 1] = count
# print(s)
# for i in range(len(s) - 1):
#     if a < s[0]:
#         nums1.append(a)
#         nums1 += s
#         break
#     else:
#         nums1.append(s[0])
#         s.pop(0)
# print(nums1)
#
# # 方法二
# s = [1, 4, 6, 9, 13, 16, 19, 28, 40, 100]
# print("原始列表", s)
#
#
# def add():
#     num = int(input("插入一个数字:"))
#     s.append(num)
#
#
# def sort():
#     s.sort()
#
#
# add()
# sort()
# print("排序后的列表", s)


# 2.选择省市区
dic = {
    "江西": {
        "萍乡": ["安源", "彭高", "上栗"],
        "新余": ["良山", "新钢", "兴安岭"],
    },
    "北京": {
        "大兴区": ["礼贤镇", "魏善庄镇", "北臧村镇"],
        "昌平区": ["沙河", "化庄", "白浮泉"],
    },
    "福建": {
        "莆田": ["湄洲岛", "西天尾", "九化山"],
        "厦门": ["湖里", "思明", "翔安"],
    }
}
print('可查询的省份：福建、山东、广东')

# 让用户输入要查询的省份。
while True:
    province = input('请输要查询的省份：')

    # 当用户输入的省份不在要查询的字典中时，跳出本次循环，继续让用户输入。
    if not province in dic:
        print('输入错误，请重新输入')
        continue

    # 当用户输入的要查询的省份在字典中时，跳出循环。
    break

# 将用户输入的省份去取出字典中的指定的省份（键）的值——市级字典，
# 然后遍历每个市级字典，遍历的的结果是取出市级字典中每个键。
for i in dic[province]:
    print(i, end=' ')  # 取出的市级字典中的每个城市（键），并作一行显示。

# 让用户输入要查询的城市。
while True:
    city = input('请输入要查询的城市：')

    # 当用户输入的城市不在要查询的子字典中时，跳出本次循环，继续让用户输入。
    if not city in dic[province]:
        print('输入错误')
        continue

    # 当用户输入的要查询的城市在子字典中时，跳出循环。
    break

# 将用户输入的城市去取出子字典中的指定的城市（键）的值——县级列表
# 然后遍历每个镇县级列表，遍历的的结果是取出县级列表中的每个县名。
for j in dic[province][city]:
    print(j, end=' ')

# 4.读取文件“txl.txt”的数据并显示出来，可以按关键字查询
# with open("../IO/test.xls", "r") as f:  # 打开文件
#     data = f.read()  # 读取文件
#     print(data)
