# %%
from typing import *


def merge(array: List[int], start: int, mid: int, end: int) -> None:

    left_start = start
    right_start = mid
    result = []
    while left_start < mid and right_start < end:
        if array[left_start] < array[right_start]:
            result.append(array[left_start])
            left_start += 1
        else:
            result.append(array[right_start])
            right_start += 1
    while left_start < mid:
        result.append(array[left_start])
        left_start += 1
    while right_start < end:
        result.append(array[right_start])
        right_start += 1
    for i in range(len(result)):
        array[start+i] = result[i]


def merge_sort(array: List[int], start: int, end: int) -> None:
    if start < end-1:
        mid = (start+end)//2
        merge_sort(array, start, mid)
        merge_sort(array, mid, end)
        merge(array, start, mid, end)


def test_merge_sort():
    array = [6, 7, 8, 9, 1, 2, 3, 4, 5,  10]
    merge_sort(array, 0, len(array))
    print(array)


if __name__ == '__main__':
    test_merge_sort()

# %%
