class Person11:
    def __init__(self, name):
        self.__name = name
    @property
    def name(self):
        return self.__name
#测试代码
p = Person11('王五')
print(p.name)
