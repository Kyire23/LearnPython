"""
@Author = oumuamuanode
@Time : 2022/10/27 16:26
"""


# 单继承
# 类定义 class people(object): 新式写法

class People:
    def __init__(self, n, a, w):
        self.name = n
        self.age = a;
        self.__weight = w

    def speak(self):
        print(str.format("{0}说:我{1}岁", self.name, self.age))


class Student(People):
    def __init__(self, n, a, w, g):
        super().__init__(n, a, w)
        self.grade = g

    def speak(self):
        print(str.format("{0}说:我{1}岁,我在读{2}年级", self.name, self.age, self.grade))


s = Student("小华", 10, 60, 3)
s.speak()

