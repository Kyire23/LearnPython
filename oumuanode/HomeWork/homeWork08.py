"""
@Author = oumuamuanode
@Time : 2022/10/28 21:01
"""


class Shape:
    def __init__(self):
        pass

    def area(self, shape):
        shape.area()


class Rectangle:
    def __init__(self, c, k):
        self.c = c
        self.k = k

    def area(self):
        print(str.format('长:{0},宽:{1}的矩形面积是：{2}', self.c, self.k, self.c * self.k))


class Triangle:
    def __init__(self, d, g):
        self.d = d
        self.g = g

    def area(self):
        print(str.format('底:{0},高:{1}的三角形面积是：{2}', self.d, self.g, self.d * self.g / 2))


class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        print(str.format('半径:{0}的圆面积是：{1}', self.r, 3.14*self.r**2))


c = Shape()
c.area(Rectangle(3,4))
c.area(Rectangle(5,4))
c.area(Triangle(5,6))
c.area(Circle(1))
c.area(Circle(2))