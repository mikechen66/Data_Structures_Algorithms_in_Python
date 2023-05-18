

# quick_queue_pivot.py


from linked_queue_iter import LinkedQueue


def quick_sort(arr, i, j):
    if i >= j:
        return arr
    pivot = arr[i]
    low = i
    high = j
    while i < j:
        while i < j and arr[j] >= pivot:
            j -=1
        arr[i] = arr[j]
        while i < j and arr[i] <= pivot:
            i += 1
        arr[j] = arr[i]
    arr[i] = pivot
    quick_sort(arr, low, i-1)
    quick_sort(arr, i+1, high)
    return arr


if __name__ == '__main__':
    lq = LinkedQueue()
    lq.enqueue(7)
    lq.enqueue(6)
    lq.enqueue(5)
    lq.enqueue(4)
    lq.enqueue(3)
    lq.enqueue(2)
    lq.enqueue(1)
    lq.dequeue()
    res1 = [i for i in lq]
    print(res1)
    res2 = quick_sort(res1, 0, len(res1)-1)
    print(res2)


# Output:

 """
 7
[6, 5, 4, 3, 2, 1]
[1, 2, 3, 4, 5, 6]
 """