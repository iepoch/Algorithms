#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

# key:value
# n : value of term


def eating_cookies(n, cache={}):

    # start with base case of
    # Second Solution of eating cookies like the original
    if n == 0:
        return 1
    elif n < 3:
        return n
    elif n in cache:
        return cache[n]
    else:
        value = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
        cache[n] = value
        return value

 # Working Solution
    # if n == 0:
    #     return 1
    # elif n < 3:  # if n is less then 3 then return what it is
    #     return n
    # elif cache and cache[n] > 0:
    #     return cache[n]
    # else:
    #     if not cache:
    #         cache = {i: 0 for i in range(n+1)}  # creating cache of n
    #     cache[n] += eating_cookies(n-1, cache) + \
    #         eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    #     return cache[n]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
