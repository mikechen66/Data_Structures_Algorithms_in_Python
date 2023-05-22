

# mergesort.py


def merge(left, right):
    # 合并两个有序列表
    res = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    if left:
        res.extend(left)
    if right:
        res.extend(right)
    return res


def mergesort(arr):
    n = len(arr)
    if n < 2:
        return arr
    middle = n // 2
    left = arr[:middle] 
    right = arr[middle:]
    left_sort = mergesort(left) 
    right_sort = mergesort(right)
    return merge(left_sort, right_sort)


if __name__ == '__main__':
    mergesort([11, 99, 33 , 69, 77, 88, 55, 11, 33, 36,39, 66, 44, 22])
