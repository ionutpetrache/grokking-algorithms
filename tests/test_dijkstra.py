# -*- coding: utf-8 -*-


import algorithms.djikstra as lib

graph = {"start": {"a": 5, "b": 2}, "a": {"c": 4, "d": 2}, "b": {"a": 8, "d": 7},
         "c": {"finish": 3, "d": 6}, "d": {"finish": 1}, "finish": {}}


def test_dijkstra_01():
    result = lib.find_shortest_path(graph, "start", "finish")

    assert result == 8
