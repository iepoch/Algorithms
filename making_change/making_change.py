#!/usr/bin/python

import sys


def making_change(amount, denominations):
    if amount == 0:
        return 1
    elif amount < 3:
        # denominations[amount] = amount
        return amount
    elif denominations and denominations[amount] > 0:
        return denominations[amount]
    else:
        if not denominations:
            denominations = {i: 0 for i in range(amount+1)}
            # 3 recursive calls # amount-1, amount-2, amount-3
            denominations[amount] += making_change(amount-1, denominations) + making_change(
                amount-2, denominations) + making_change(amount-3, denominations)
    print(f'The num {amount}')
    return denominations[amount]


if __name__ == "__main__":
        # Test our your implementation from the command line
        # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
