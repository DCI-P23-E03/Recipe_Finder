import csv
from add_recipe import add_recipe_to_csv

file_path = '/home/user/Documents/DCI_CODE/assignments2023/Recipe_Finder/RecipeNLG_dataset_smaller.csv'
recipe_number = "99"
title = 'Kartoffelsalat'
ingredients = ['Kartoffel', 'Milk', 'Eggs', 'Sugar', 'Butter']
directions = ['Mix dry ingredients', 'Whisk eggs and milk', 'Combine wet and dry ingredients']
link = 'https://www.example.com/pancakes-recipe'
source = 'Example Recipes'
keywords = ['pancakes', 'breakfast', 'brunch']

add_recipe_to_csv(file_path,recipe_number, title, ingredients, directions, link, source, keywords)


