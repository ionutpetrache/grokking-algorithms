# -*- coding: utf-8 -*-


import algorithms.binary_search as lib


def test_binary_search_01():
    data = [1, 2, 3, 4, 5, 10, 22, 33, 44, 55, 66, 77, 88, 99, 200, 300]

    result = lib.search(data, 50)

    assert result is None


def test_binary_search_02():
    data = [1, 2, 3, 4, 5, 10, 22, 33, 44, 55, 66, 77, 88, 99, 200, 300]

    result = lib.search(data, 66)

    assert result == 10


def test_binary_search_03():
    data = [1, 2, 3, 4, 5, 10, 22, 33, 44, 55, 66, 77, 88, 99, 200, 300]

    result = lib.search(data, -1)

    assert result is None


def test_binary_search_04():
    data = [1, 2, 3, 4, 5, 10, 22, 33, 44, 55, 66, 77, 88, 99, 200, 300]

    result = lib.search(data, 0)

    assert result is None


def test_binary_search_05():
    data = [1, 2, 3, 4, 5, 10, 22, 33, 44, 55, 66, 77, 88, 99, 200, 300]

    result = lib.search(data, 1)

    assert result == 0


def test_binary_search_06():
    data = [1, 2, 3, 4, 5, 10, 22, 33, 44, 55, 66, 77, 88, 99, 200, 300]

    result = lib.search(data, 2)

    assert result == 1


def test_binary_search_07():
    data = [1, 2, 3, 4, 5, 10, 22, 33, 44, 55, 66, 77, 88, 99, 200, 300]

    result = lib.search(data, 200)

    assert result == 14


def test_binary_search_08():
    data = [1, 2, 3, 4, 5, 10, 22, 33, 44, 55, 66, 77, 88, 99, 200, 300]

    result = lib.search(data, 300)

    assert result == 15


def test_binary_search_09():
    data = [1, 2, 3, 4, 5, 10, 22, 33, 44, 55, 66, 77, 88, 99, 200, 300]

    result = lib.search(data, 1000)

    assert result is None


def test_binary_search_10():

    result = lib.search(None, 20)

    assert result is None


def test_binary_search_11():
    data = [1, 2, 3, 4, 5, 10, 22, 33, 44, 55, 66, 77, 88, 99, 200, 300]

    result = lib.search(data, None)

    assert result is None


def test_binary_search_12():
    data = [-200, -100, 0, 100, 200, 300]

    result = lib.search(data, 0)

    assert result == 2
