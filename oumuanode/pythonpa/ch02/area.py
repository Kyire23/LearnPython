import math
a = 3.0
b = 4.0
c = 5.0
h = (a + b + c) / 2                       #三角形周长的一半
s = math.sqrt(h*(h-a)*(h-b)*(h-c))        #三角形面积
print(s)
