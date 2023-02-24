#chapter03\if_3desc.py

a = int(input("请输入整数a："))
b = int(input("请输入整数b："))
c = int(input("请输入整数c："))
if (a < b): t = a; a = b; b = t   #使得a>b
if (a < c): t = a; a = c; c = t   #使得a>c
if (b < c): t = b; b = c; c = t   #使得b>c
print("排序结果（降序）：", a, b, c)



input()
