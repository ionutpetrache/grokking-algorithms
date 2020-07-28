# -*- coding: utf-8 -*-

import math


def _initialize_data(graph, start_node):
    processes = []
    costs = {}
    parents = {}
    for parent in graph:
        costs[parent] = math.inf
    costs[start_node] = 0
    return costs, parents, processes


def _find_next_node_to_check(costs, processed):
    lowest_cost = math.inf
    node_with_lowest_cost = None

    for node in costs:
        if costs[node] < lowest_cost and node not in processed:
            lowest_cost = costs[node]
            node_with_lowest_cost = node
    return node_with_lowest_cost


def find_shortest_path(graph, start_node, finish_node):
    # initialize
    costs, parents, processed = _initialize_data(graph, start_node)

    # starting ...
    node = _find_next_node_to_check(costs, processed)
    while node:
        neighbours = graph[node]
        for n in neighbours.keys():
            if costs[n] > costs[node] + neighbours[n]:
                costs[n] = neighbours[n] + costs[node]
                parents[n] = node
        processed.append(node)
        node = _find_next_node_to_check(costs, processed)
    return costs[finish_node]
