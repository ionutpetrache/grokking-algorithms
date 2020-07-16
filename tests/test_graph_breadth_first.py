# -*- coding: utf-8 -*-

import algorithms.graph as lib


def create_graph():
    graph = {"you": ["alice", "bob", "claire"], "bob": ["anuj", "peggy"], "alice": ["peggy"],
             "claire": ["thom", "jonny"], "anuj": [], "peggy": [], "thom": [], "jonny": []}
    return graph


def test_breadth_first_should_find_person_when_present_01():
    graph = create_graph()

    result = lib.search(graph, "you", "peggy")

    assert result


def test_breadth_first_should_find_person_when_present_02():
    graph = create_graph()

    result = lib.search(graph, "you", "you")

    assert result


def test_breadth_first_should_find_person_when_present_03():
    graph = create_graph()

    result = lib.search(graph, "you", "jonny")

    assert result


def test_breadth_first_should_return_false_when_person_not_present_04():
    graph = create_graph()

    result = lib.search(graph, "you", "gigi")

    assert result is False
