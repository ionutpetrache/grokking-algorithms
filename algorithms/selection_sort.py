# -*- coding: utf-8 -*-

from typing import List


def _find_smallest(data: List[int]):
    if len(data) <= 0:
        return
    smallest_index = 0
    smallest_value = data[smallest_index]
    for i, e in enumerate(data):
        if e < smallest_value:
            smallest_index = i
            smallest_value = data[smallest_index]
    return smallest_index, smallest_value


def sort_in_place(data: List[int]):
    if not data:
        return None

    for index, value in enumerate(data):
        smallest_index, smallest_value = _find_smallest(data[index:])
        tmp = data[index]
        data[index] = smallest_value
        data[index + smallest_index] = tmp
    return data


def sort_with_new_array(data: List[int]):
    if not data:
        return None

    result = []

    for i in range(len(data)):
        smallest_index, smallest_value = _find_smallest(data)
        result.append(smallest_value)
        data.pop(smallest_index)
    return result


