#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    pass
    # Set to empty list of list because you can start with nothing
    possible = [[]]
    allPoss = []  # All possibilities to be stored here
    cache = {0: 1}  # Cache recursion to stop making so many calls
    # Set the options to be stored for latter
    options = [['rock'], ['paper'], ['scissors']]

    if n == 0:
        return possible
    elif n in cache:
        return cache[n]
    else:

        before = rock_paper_scissors(n-1)
        cache[n] = before

        # print(cache[n]) Checking to see if it's been cached

        for pos in cache[n]:
            for option in options:
                allPoss.append(pos + option)
    # print(f'All possible ways: \n{allPoss}\n')  Viewing what is getting printed
    return allPoss


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
