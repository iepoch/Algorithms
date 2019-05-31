#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    allPossibilities = []  # All possibilities list
    # We will want some recurision for this
    # Need to pass the list to each recurision call
    # To concantate two list together
    # Define an inner recursive helper
    options = [['rock'], ['paper'], ['scissors']]
    if n == 0:
        return [[]]
    else:
        prevPoss = rock_paper_scissors(n-1)

        for poss in prevPoss:
            for o in options:
                allPossibilities.append(poss + o)
            # allPossibilities.extend(somePoss)
    return allPossibilities


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
