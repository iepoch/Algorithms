#!/usr/bin/python

import argparse


def find_max_profit(prices):
    pass

    max_profits = None

    for i in range(len(prices) - 1):
        buy = prices[i]
        sell = i + 1

        for j in prices[sell:]:
            profit = j - buy

            if max_profits == None or profit > max_profits:
                max_profits = profit
    print(f'This is max profit {max_profits}')
    return max_profits


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
