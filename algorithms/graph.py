# -*- coding: utf-8 -*-

from collections import deque


def search(graph, first_element, look_for_name):
    searched_names = []
    q = deque()

    q.append(first_element)
    while q:
        first = q.popleft()
        if first not in searched_names:
            if first == look_for_name:
                return True
            else:
                q.extend(graph[first])
                searched_names.append(first)
    return False
