#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    pass

    curr_val = math.inf  # inital value for optimization

    for amount, value in recipe.items():
        # Checking for what is returned here print(amount, value)
        if amount not in ingredients:
            return 0
        value = ingredients[amount] // value
       # Printing out what the amounts are deviding by
        print(
            f'this is new value from deviding recipe value {ingredients[amount]}  = {value}')
        if value == 0:
            return 0
        elif value <= curr_val:
            curr_val = value

    return curr_val


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
