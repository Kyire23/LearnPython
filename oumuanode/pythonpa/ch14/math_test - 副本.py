import math
#三角形三边a、b、c，必须满足：a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a
a=int(input("请输入边长a："))
b=int(input("请输入边长b："))
c=int(input("请输入边长c："))
if (a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a):
    h = (a + b + c) / 2                  #周长的一半
    area = math.sqrt(h * (h - a) * (h - b) * (h - c))  #面积
    perimeter = a + b + c                     #周长
    height_a = 2 * area / a      #边长a所对应的高
    max_side = max(a, b, c)     #最长边长
    min_side = min(a, b, c)     #最短边长
    print(area,perimeter,height_a,max_side,min_side)
else:
    print("不能构成三角形！")
