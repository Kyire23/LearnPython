# def ispoitive(num):
#     try:
#         float(num)
#     except:
#         return False;
#     else:
#         if float(num) <= 0:
#             return False
#         else:
#             return True
#
# # 直角三角形的判断
# def isRightTriangle(num1,num2,num3):
#     if num1**2 +num2**2 == num3**2 +num3**2 or num2**2 +num3**2 == num1**2:
#         return True
#     else:
#         return False
#
# a = input("输入第一个数字:")
# while not ispoitive(a):
#     a = input("error")
# b = input("输入第二个数字:")
# while not ispoitive(b):
#     b= input("error")
# c =input("输入第三个数字:")
# while not ispoitive(c):
#     c = input("error")
#
# a= float(a)
# b = float(b)
# c = float(c)
#
# if a+b >c and a+c >b and b+c>a:
#     if a==b ==c:
#         print('%.2f,%.2f,%.2f能组成等边三角形'%(a,b,c))
#     elif a==b or a==c or b==c:
#         if isRightTriangle(a,b,c):
#             print('%.2f,%.2f,%.2f能组成等腰直角三角形'%(a,b,c))
#         else:
#             print('%.2f,%.2f,%.2f能组成等腰三角形' % (a, b, c))
#     elif isRightTriangle(a,b,c):
#         print('%.2f,%.2f,%.2f能组成直角三角形' % (a, b, c))
#     else:
#         print('%.2f,%.2f,%.2f能组成普通三角形' % (a, b, c))
# else:
#         print('%.2f,%.2f,%.2f不能组成三角形' % (a, b, c))
# def app(a, b):
#     x = (4 * a - b) / 2
#     if a != 0 and (4 * a - b) % (x * 2) == 0:
#         y = a - x
#         if x < 0 or y < 0:
#             print("{}只动物{}条腿的情况无解".format(a, b))
#         else:
#             print("鸡有{}只，兔有{}只".format(int(x), int(y)))
#     else:
#         print("{}只动物{}条腿的情况无解".format(a, b))
#
#
# a = input("请输入鸡和兔的总数\n")
# b = input("请输入鸡和兔的脚数\n")
#
# a = int(a)
# b = int(b)
#
# app(a, b)

# far = [100]
#
#
# def jump(n):
#     if n == 1:
#         far.append(100)
#         return 50
#     else:
#         b = jump(n - 1) / 2
#         far.append(b * 2)
#         return b
#
#
# print(jump(10))
# print(far)
# print(sum(far) - jump(10))

far= []
high = 100
for i in range(1,11):
    if i == 1:
        far.append(high)
    else:
        far.append(high*2)
    high = high/2
print(str.format('小球第10次落地时经过的总距离:{0}米',sum(far)))
print(str.format('第十次反弹的高度是:{0}米',high))
