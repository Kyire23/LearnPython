def unique(items):
    items_existed = set()
    for item in items:
        if item not in items_existed:
            yield item
            items_existed.add(item)
if __name__ == "__main__":
    #测试代码
    a = [1, 8, 5, 1, 9, 2, 1, 10]
    a1 = unique(a)
    print(list(a1))
