def _binarySearch(key, a, lo, hi):
    if hi <= lo: return -1  # 查找失败，返回-1
    mid = (lo + hi) // 2  # 计算中间位置
    if a[mid] > key:  # 中间位置项目大于查找关键字
        return _binarySearch(key, a, lo, mid)  # 递归查找前一子表
    elif a[mid] < key:  # 中间位置项目小于查找关键字
        return _binarySearch(key, a, mid + 1, hi)  # 递归查找后一子表
    else:  # 中间位置项目等于查找关键字
        return mid  # 查找成功，返回下标位置


def binarySearch(key, a):  # 二分查找
    return _binarySearch(key, a, 0, len(a))  # 递归二分查找法


def main():
    a = [1, 13, 26, 33, 45, 55, 68, 72, 83, 99]
    x = int(input("请输入整数x："))
    print(binarySearch(x, a))  # 二分查找关键字


if __name__ == '__main__': main()
