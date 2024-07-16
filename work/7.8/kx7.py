# 归并排序
from heapq import merge


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

print(merge_sort([3, 2, 1, 4, 5, 6, 7, 8, 9, 0])