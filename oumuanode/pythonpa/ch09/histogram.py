import random
import math


class Stat:
    def __init__(self, n):
        self._data = []
        for i in range(n):
            self._data.append(0)

    def addDataPoint(self, i):
        """增加数据点"""
        self._data[i] += 1

    def count(self):
        """计算数据点个数之和（统计数据点个数）"""
        return sum(self._data)

    def mean(self):
        """计算各数据点个数的平均值"""
        return sum(self._data) / len(self._data)

    def max(self):
        """计算各数据点个数的最大值"""
        return max(self._data)

    def min(self):
        """计算各数据点个数的最小值"""
        return min(self._data)

    def draw(self):
        """绘制简易直方图"""
        for i in self._data:
            print('#' * i)


# 测试代码
if __name__ == '__main__':
    # 随机生成100个的0到9的数
    st = Stat(10)
    for i in range(100):
        score = random.randrange(0, 10)
        st.addDataPoint(math.floor(score))
    print('数据点个数：{}'.format(st.count()))
    print('数据点个数的平均值：{}'.format(st.mean()))
    print('数据点个数的最大值：{}'.format(st.max()))
    print('数据点个数的最小值：{}'.format(st.min()))
    st.draw()  # 绘制简易直方图
