# -*- coding: utf-8 -*-

import algorithms.exercises as lib


def test_sum_array():
    data = [1, 2, 3, 4]

    result = lib.sum_array(data)

    assert result == 10


def test_count_elements_01():
    data = [1, 2, 3, 4, 5]

    result = lib.count_elements(data)

    assert result == 5


def test_count_elements_02():
    data = None

    result = lib.count_elements(data)

    assert result == 0


def test_find_maximum_01():
    data = [1, 2, 3, 20, 4, 5]

    result = lib.find_maximum(data)

    assert result == 20


def test_find_maximum_02():
    data = []

    result = lib.find_maximum(data)

    assert result is None


def test_binary_search_01():
    data = [1, 2, 3, 4, 5, 6]

    assert 1 == lib.binary_search(data, 2)

    assert 0 == lib.binary_search(data, 1)

    assert 5 == lib.binary_search(data, 6)

    assert 4 == lib.binary_search(data, 5)