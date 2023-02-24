"""
@Author = oumuamuanode
@Time : 2022/10/27 16:36
"""


class People:
    name = ''
    age = 0
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a;
        self.__weight = w

    def speak(self):
        print(str.format("{0}说:我{1}岁", self.name, self.age))


class Student(People):
    grade = ''

    def __init__(self, n, a, w, g):
        super().__init__(n, a, w)
        self.grade = g

    def speak(self):
        print(str.format("{0}说:我{1}岁,我在读{2}年级", self.name, self.age, self.grade))


# 多继承

class Speaker():

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print(str.format("我叫{0},我是一个演说家,我演讲的主题是{1}", self.name, self.topic))


class Sample(Speaker, Student):

    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)


test = Sample("小凡", 25, 80, 4, "我的祖国")
test.speak()
