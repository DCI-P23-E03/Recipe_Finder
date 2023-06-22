import csv
import os
###file_path = 'RecipeNLG_dataset_smaller.csv'

def search_recipe_by_title(file_path):
    keyword = input("Enter a keyword to search in recipe titles: ").lower()

    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        found_recipes = []
        for row in reader:
            if row and keyword in row[1].lower():
                found_recipes.append((row[0], row[1]))

    if found_recipes:
        print(f"Recipes containing the keyword '{keyword}':")
        for recipe in found_recipes:
            print(f"Recipe Number: {recipe[0]}, Title: {recipe[1]}")
    else:
        print(f"No recipes found containing the keyword '{keyword}'.")

def delete_recipe(file_path):
    search_recipe_by_title(file_path)
    recipe_number = input("Enter the recipe number to delete: ")

    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    deleted_recipe = None

    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in rows:
            if row and row[0] == recipe_number:
                deleted_recipe = row
            else:
                writer.writerow(row)

    if deleted_recipe:
        print(f"Recipe Number: {deleted_recipe[0]}, Title: {deleted_recipe[1]} has been deleted.")
    else:
        print(f"No recipe found with the number {recipe_number}.")

    # Check if the file was deleted
    if not os.path.exists(file_path):
        print("The file was deleted successfully.")

#search_recipe_by_title(file_path)
#delete_recipe(file_path)





