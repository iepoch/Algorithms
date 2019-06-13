#!/usr/bin/python

import argparse


def find_max_profit(prices):
    pass
    max_profit = None

    for i in range(0, len(prices) - 1):
        curr_profit = prices[i]
        sell_price = i + 1
        print(curr_profit)

        for j in prices[sell_price:]:
            profit = j - curr_profit
            print([profit])

            if max_profit == None or profit > max_profit:
                max_profit = profit

    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
