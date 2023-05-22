

# merge_sort_inplace.py



import time


def reverse(arr, i, index, j):
    list1 = arr[i:index]
    reverse_list1 = list(reversed(list1))  
    list2 = arr[index:j]
    reverse_list2 = list(reversed(list2))  
    list3 = list(reversed(reverse_list1 + reverse_list2)) 
    list4 = arr[0:i] + list3 + arr[j:]  
    for i in range(len(list4)):
        arr[i] = list4[i]
    return arr


def merge(arr, l, m, h):
    i = l
    j = m + 1
    while i < j and j <= h:
        while i < j and arr[i] <= arr[j]:
            i += 1
        index = j
        while j <= h and arr[j] < arr[i]:
            j += 1
        # print("low: {},index:{},high:{}".format(i, index, j))
        arr = reverse(arr, i, index, j)
        i = i + (j - index)
    return arr


def merge_sort(arr, l, h):
    if l < h:
        mid = l + (h - l) // 2
        merge_sort(arr, l, mid)
        merge_sort(arr, mid + 1, h)
        result = merge(arr, l, mid, h)
        return result


if __name__ == '__main__':
    user_input = input('Input 10 integers with colon seperation：\n').strip()
    data=[int(item) for item in user_input.split(',')]
    print("before sorting: ", data)
    start = time.perf_counter()
    result = merge_sort(data, 0, len(data) - 1)
    print("after sorting：", result)
    end = time.perf_counter()
    print("Time consumed：", end - start)


# Output:

"""
Input 10 integers with colon seperation：
20,18,19,16,17,14,15,12,13,11,10
before sorting:  [20, 18, 19, 16, 17, 14, 15, 12, 13, 11, 10]
after sorting： [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Time consumed： 0.00015604399999347152
"""