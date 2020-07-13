# -*- coding: utf-8 -*-

from typing import List, Any


# 4.1 Write out the code for the earlier sum function.
def sum_array(arr_data: List[int]):
    if arr_data is None or arr_data == []:
        return 0
    else:
        return arr_data[0] + sum_array(arr_data[1:])


# 4.2 Write a recursive function to count the number of items in a list.
def count_elements(arr_data: List[Any]):
    if not arr_data:
        return 0
    else:
        return 1 + count_elements(arr_data[1:])


# 4.3 Find the maximum number in a list.
def find_maximum(arr_data: List[int]):
    def maximum(a, b):
        return a if a > b else b

    if not arr_data:
        return None

    if len(arr_data) == 1:
        return arr_data[0]
    else:
        return maximum(arr_data[0], find_maximum(arr_data[1:]))


# 4.4 Remember binary search from chapter 1? It’s a divide-and-conquer
# algorithm, too. Can you come up with the base case and recursive
# case for binary search?
def binary_search(data: List[int], value: int):
    def bs(initial_list, low_index, high_index, val):
        if low_index > high_index:
            return None

        middle_index = (low_index + high_index) // 2

        if initial_list[middle_index] > val:
            # value is on lower part
            return bs(initial_list, low_index, middle_index - 1, val)
        elif initial_list[middle_index] < val:
            # value is on upper part
            return bs(initial_list, middle_index + 1, high_index, val)
        else:
            return middle_index

    if not data or value is None:
        return None
    return bs(data, 0, len(data) - 1, value)
