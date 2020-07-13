# -*- coding: utf-8 -*-

from typing import List


def sort(data: List[int]):
    def partition(array, pi):
        ls = [i for i in array[(pi + 1):] if i <= array[pi]]
        gr = [i for i in array[(pi + 1):] if i > array[pi]]
        return ls, gr

    pivot_index = 0
    if not data or len(data) < 2:
        return data
    else:
        less, greater = partition(data, pivot_index)
        return sort(less) + [data[pivot_index]] + sort(greater)
