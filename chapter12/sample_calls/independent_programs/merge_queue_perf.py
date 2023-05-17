
# merge queue performace 

# merge_queue_perf.py


import timeit
from random import randint
from collections import deque


def merge_of_two_sorted_array(nums, left, mid, right):
    for index in range(left, right + 1):
        nums_for_compare[index] = nums[index]
    i = left
    j = mid + 1
    for k in range(left, right + 1):
        if i == mid + 1:
            nums[k] = nums_for_compare[j]
            j += 1
        elif j > right:
            nums[k] = nums_for_compare[i]
            i += 1
        elif nums_for_compare[i] < nums_for_compare[j]:
            nums[k] = nums_for_compare[i]
            i += 1
        else:
            assert nums_for_compare[i] >= nums_for_compare[j]
            nums[k] = nums_for_compare[j]
            j += 1


def merge_sort(nums):
    l = len(nums)
    global nums_for_compare
    nums_for_compare = list(range(l))
    sz = 1
    # sz = 1, 2, 4, 8
    while sz < l:
        # left = 0, 2, 4, 6
        left = 0
        while left < l - sz:
            merge_of_two_sorted_array(nums, left, left + sz - 1, min(left + sz + sz - 1, l - 1))
            left += 2 * sz
        sz *= 2


def queue_merge(array):
    merge_queue = deque()
    while len(array) > 1:
        one = array.pop()
        other = array.pop()
        if one < other:
            merge_list = [one, other]
            merge_queue.appendleft(merge_list)
        else:
            merge_list = [other, one]
            merge_queue.appendleft(merge_list)
    if array:
        merge_queue.appendleft([array.pop()])
    while len(merge_queue) > 1:
        merge_list1 = merge_queue.pop()
        merge_list2 = merge_queue.pop()
        l = 0
        r = 0
        new_list = []
        while l < len(merge_list1) and r < len(merge_list2):
            if merge_list1[l] < merge_list2[r]:
                new_list.append(merge_list1[l])
                l += 1
            else:
                new_list.append(merge_list2[r])
                r += 1
        new_list += merge_list1[l:]
        new_list += merge_list2[r:]
        merge_queue.appendleft(new_list)
    return merge_queue.pop()


def quick_sort(lists, i, j):
    if i >= j:
        return lists
    pivot = lists[i]
    low = i
    high = j
    while i < j:
        while i < j and lists[j] >= pivot:
            j -= 1
        lists[i] = lists[j]
        while i < j and lists[i] <= pivot:
            i += 1
        lists[j] = lists[i]
    lists[j] = pivot
    quick_sort(lists, low, i - 1)
    quick_sort(lists, i + 1, high)
    return lists


def generate_random_array(n, min, max):
    arr = [randint(min, max,) for i in range(n)]
    return arr


if __name__ == '__main__':
    int_num = 1000000
    last = int_num - 1
    max = 1000000
    try_num = 1
    print('MergeSort: ', timeit.timeit("merge_sort({})".format(generate_random_array(int_num, 0, max)),
                                     setup="from __main__ import merge_sort",
                                     number=try_num))
    print('QueueMerge:', timeit.timeit("queue_merge({})".format(generate_random_array(int_num, 0, max)),
                                      setup="from __main__ import queue_merge",
                                      number=try_num))
    print('QuickSort: ', timeit.timeit("quick_sort({},{},{})".format(generate_random_array(int_num, 0, int_num), 0, last),
                                      setup="from __main__ import quick_sort",
                                      number=try_num))


# Output:

"""
MergeSort:  10.722240050999972
QueueMerge: 7.716620402999979
QuickSort:  4.428637085999981
"""