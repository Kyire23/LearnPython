def bubbleSort(a):
    for i in range(len(a) - 1, 0, -1):  # 外循环
        for j in range(i):  # 内循环
            if a[j] > a[j + 1]:  # 大数往下沉
                a[j], a[j + 1] = a[j + 1], a[j]
        # print(a)    #跟踪调试


def main():
    a = [2, 97, 86, 64, 50, 80, 3, 71, 8, 76]
    bubbleSort(a)
    print(a)


if __name__ == '__main__': main()
