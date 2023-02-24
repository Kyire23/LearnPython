# import random
#
# num = range(0, 100)
#
# nums = random.sample(num, 10)
# print(nums)
# print(min(nums))
# print(max(nums))

def bubble_sort(nums):
    count = len(nums)
    for i in range(0, count):
        for j in range(i + 1, count):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums;


def insert_sort(nums):
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] < nums[j]:
                nums.insert(j, nums.pop(i))
                break
    return nums


nums = insert_sort([4, 5, 6, 7, 3, 2, 6, 9, 8])
print(nums)


def sell_sort(nums):
    gap = len(nums)
    while gap > 1:
        gap = gap // 2
        for i in range(gap, len(nums)):
            for j in range(i % gap, i, gap):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums


nums = sell_sort([4, 5, 6, 7, 3, 2, 6, 9, 8])
print(nums)


def quick_sort(qlist):
    if qlist == []:
        return []
    else:
        qfirst = qlist[0]
        qless = quick_sort([l for l in qlist[1:] if l < qfirst])
        qmore = quick_sort([m for m in qlist[1:] if m >= qfirst])
        return qless + [qfirst] + qmore


qlist = quick_sort([4, 5, 6, 7, 3, 2, 6, 9, 8])
print(qlist)


def select_sort(slist):
    for i in range(len(slist) - 1):
        x = i
        for j in range(i, len(slist)):
            if slist[j] < slist[x]:
                x = j
        slist[i], slist[x] = slist[x], slist[i]
    return slist


slist = select_sort([4, 5, 6, 7, 3, 2, 6, 9, 8])
print(slist)

import copy


def heap_sort(hlist):
    def heap_adjust(parent):
        child = 2 * parent + 1  # left child
        while child < len(heap):
            if child + 1 < len(heap):
                if heap[child + 1] > heap[child]:
                    child += 1  # right child
            if heap[parent] >= heap[child]:
                break
            heap[parent], heap[child] = heap[child], heap[parent]
            parent, child = child, 2 * child + 1

    heap, hlist = copy.copy(hlist), []
    for i in range(len(heap) // 2, -1, -1):
        heap_adjust(i)
    while len(heap) != 0:
        heap[0], heap[-1] = heap[-1], heap[0]
        hlist.insert(0, heap.pop())
        heap_adjust(0)
    return hlist


hlist = heap_sort([4, 5, 6, 7, 3, 2, 6, 9, 8])
print(hlist)


def radix_sort(array):
    bucket, digit = [[]], 0
    while len(bucket[0]) != len(array):
        bucket = [[], [], [], [], [], [], [], [], [], []]
        for i in range(len(array)):
            num = (array[i] // 10 ** digit) % 10
            bucket[num].append(array[i])
        array.clear()
        for i in range(len(bucket)):
            array += bucket[i]
        digit += 1
    return array


def merge_sort(array):
    def merge_arr(arr_l, arr_r):
        array = []
        while len(arr_l) and len(arr_r):
            if arr_l[0] <= arr_r[0]:
                array.append(arr_l.pop(0))
            elif arr_l[0] > arr_r[0]:
                array.append(arr_r.pop(0))
        if len(arr_l) != 0:
            array += arr_l
        elif len(arr_r) != 0:
            array += arr_r
        return array

    def recursive(array):
        if len(array) == 1:
            return array
        mid = len(array) // 2
        arr_l = recursive(array[:mid])
        arr_r = recursive(array[mid:])
        return merge_arr(arr_l, arr_r)

    return recursive(array)