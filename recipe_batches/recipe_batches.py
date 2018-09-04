#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    max_batches = 0
    for ingredient in recipe:
        if ingredient not in ingredients:
            return 0
        batches = int(ingredients[ingredient] / recipe[ingredient])
        if not batches:
            return 0
        if batches > max_batches and max_batches < 1:
            max_batches = batches   
    return max_batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))