import math
a = float(input("请输入三角形的边长a："))
b = float(input("请输入三角形的边长b："))
c = float(input("请输入三角形的边长c："))
h = (a + b + c) / 2          #三角形周长的一半
area = math.sqrt(h*(h-a)*(h-b)*(h-c));#三角形面积
print(str.format("三角形三边分别为：a={0:2.0f},b={1:2.0f},c={2:2.0f}", a, b, c))
print(str.format("三角形的面积 = {0:2.0f}", area))
input()
