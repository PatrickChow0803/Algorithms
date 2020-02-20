#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    batches = float('inf') # Sets batches = to infinity.
    for item in recipe:
        try:
            recipe_amount = recipe[item]
            ingredients_amount = ingredients[item]
            compare = ingredients_amount // recipe_amount
            if compare < batches:
                batches = compare

        except KeyError:
            return 0

    return batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
