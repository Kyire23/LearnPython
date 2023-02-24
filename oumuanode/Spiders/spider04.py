class Cat:
    # 属性
    color = 'black'

    # 构造方法
    def __init__(self, name):
        self.name = name

    # 自定义方法
    def eat(self, food):
        self.food = food
        print(self.name, '正在吃' + food)

# c = Cat('Tom')
# Cat.color
# c.eat("tuzi")


# 波斯猫类
class PersianCat(Cat):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(self.name, '正在吃' + food)


# 加菲猫类
class GarfieldCat(Cat):
    def __init__(self, name):
        self.name = name

    def run(self, speed):
        print(self.name, '正在以' + speed + '的速度奔跑')


# 单继承
class SingleCat(PersianCat):
    pass


# 多继承
class MultiCat(PersianCat, GarfieldCat):
    pass


# 调用
sc = SingleCat('波斯猫1号')
sc.eat('鱼')

mc = MultiCat('波斯加菲猫1号')
mc.eat('鱼')
mc.run('50迈')
