#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


def knapsack_solver(items, capacity):
    pass
    print(sum([x[2] for x in items]) if sum([x[1]
                                             for x in items]) < capacity else 0)


cache = {}


def solve(items, capacity):

    if not items:
        return()

    if (items, capacity) not in cache:
        start = items[0]
        end = items[1:]
        include = start + solve(end, capacity-start[1])
        dont_include = solve(end, capacity)
    if knapsack_solver(include, capacity) > knapsack_solver(dont_include, capacity):
        answer = include
    else:
        answer = dont_include
    cache[(items, capacity)] = answer

    return cache[(items, capacity)]


if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')
