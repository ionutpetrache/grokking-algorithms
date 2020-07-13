# -*- coding: utf-8 -*-

from typing import List


def search(data: List[int], value: int):
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
