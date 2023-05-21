#!/usr/bin/env
#encoding=utf-8


# bucket_sort.py


def bucketSort(array):
    bucket = []
    # Create empty buckets
    for i in range(len(array)):
        bucket.append([])
    # Insert elements into their respective buckets
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)
    # Sort the elements of each bucket
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])
    # Get the sorted elements
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array


if __name__ == '__main__':
    array = [.42, .32, .33, .52, .37, .47, .51]
    print(bucketSort(array))

# Output:

"""
[0.32, 0.33, 0.37, 0.42, 0.47, 0.51, 0.52]
"""
