# -*- coding: utf-8 -*-

import algorithms.quick_sort as lib


def test_quick_sort_01():
    data = [5, 3, 1, 9, 7]

    result = lib.sort(data)

    assert result == [1, 3, 5, 7, 9]


def test_quick_sort_02():
    data = []

    result = lib.sort(data)

    assert result == []


def test_quick_sort_03():
    data = [2]

    result = lib.sort(data)

    assert result == [2]


def test_quick_sort_04():
    data = [2, 2]

    result = lib.sort(data)

    assert result == [2, 2]


def test_quick_sort_05():
    data = [3, 2]

    result = lib.sort(data)

    assert result == [2, 3]


def test_quick_sort_06():
    data = [3, 2, 6]

    result = lib.sort(data)

    assert result == [2, 3, 6]


def test_quick_sort_06():
    data = [100, 70, 60, 15, 20, 12, 13, 13, 14]

    result = lib.sort(data)

    assert result == [12, 13, 13, 14, 15, 20, 60, 70, 100]


def test_quick_sort_07():
    data = [15, 20, 14]

    result = lib.sort(data)

    assert result == [14, 15, 20]
