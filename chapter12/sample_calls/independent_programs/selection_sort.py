

# selection_sort.py 


def selection_sort(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


if __name__ == '__main__':
    data = [-2, 45, 0, 11, -9]
    size = len(data)
    selection_sort(data, size)
    print(data)


# Output:

"""
[-9, -2, 0, 11, 45]
"""