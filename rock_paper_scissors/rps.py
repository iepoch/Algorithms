#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    pass
    possible = [[]]
    allPoss = []
    cache = {0: 1}
    options = [['rock'], ['paper'], ['scissors']]

    if n == 0:
        return possible
    elif n in cache:
        return cache[n]
    else:

        before = rock_paper_scissors(n-1)
        cache[n] = before
        for pos in before:
            for option in options:
                allPoss.append(pos + option)
    print(f'All possible ways: \n{allPoss}\n')
    return allPoss


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
