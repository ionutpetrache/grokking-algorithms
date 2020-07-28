# -*- coding: utf-8 -*-

import math


def _initialize_data(graph, start_node):
    processed = []
    costs = {}
    parents = {}
    for node in graph:
        costs[node] = math.inf
    costs[start_node] = 0
    return costs, parents, processed


def _find_next_node_to_check(costs, processed):
    lowest_cost = math.inf
    node_with_lowest_cost = None

    for node in costs:
        if node not in processed and costs[node] < lowest_cost:
            lowest_cost = costs[node]
            node_with_lowest_cost = node
    return node_with_lowest_cost


def find_shortest_path(graph, start_node, finish_node):
    # initialize
    costs, parents, processed = _initialize_data(graph, start_node)

    # starting ...
    node = _find_next_node_to_check(costs, processed)
    while node:
        node_neighbours = graph[node]
        for n in node_neighbours.keys():
            current_cost_for_neighbour = costs[node] + node_neighbours[n]
            if costs[n] > current_cost_for_neighbour:
                costs[n] = current_cost_for_neighbour
                parents[n] = node
        processed.append(node)
        node = _find_next_node_to_check(costs, processed)
    return costs[finish_node]
