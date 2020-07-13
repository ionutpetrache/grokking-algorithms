# -*- coding: utf-8 -*-

import algorithms.selection_sort as lib


def test_select_01():
    data = [3, 4, 5, 6, 8, 11, 22, 33, 1, 2, 4, 4, 5, 6]

    result = lib._find_smallest(data)

    assert result == (8, 1)


def test_select_02():
    data = [5, 4]

    result = lib._find_smallest(data)

    assert result == (1, 4)


def test_select_03():
    data = [5]

    result = lib._find_smallest(data)

    assert result == (0, 5)


def test_select_04():

    data = []

    result = lib._find_smallest(data)

    assert result is None


def test_selection_sort_01():
    data = [3, 1, 2, 44, 11, 33, 55, 77, 88, 99, 100]

    result = lib.sort_with_new_array(data)

    assert result == [1, 2, 3, 11, 33, 44, 55, 77, 88, 99, 100]


def test_selection_sort_02():
    data = [99, 55, 88, 22, 77, 0, -1, 1000, -2000]

    result = lib.sort_with_new_array(data)

    assert result == [-2000, -1, 0, 22, 55, 77, 88, 99, 1000]


def test_selection_sort_03():

    result = lib.sort_with_new_array(None)

    assert result is None


def test_selection_sort_04():
    result = lib.sort_with_new_array([])

    assert result is None


def test_selection_sort_05():
    data = [3, 1, 2, 44, 11, 33, 55, 77, 88, 99, 100]

    result = lib.sort_in_place(data)

    assert result == [1, 2, 3, 11, 33, 44, 55, 77, 88, 99, 100]


def test_selection_sort_06():
    data = [99, 55, 88, 22, 77, 0, -1, 1000, -2000]

    result = lib.sort_in_place(data)

    assert result == [-2000, -1, 0, 22, 55, 77, 88, 99, 1000]


def test_selection_sort_07():

    result = lib.sort_in_place(None)

    assert result is None


def test_selection_sort_08():
    result = lib.sort_in_place([])

    assert result is None
