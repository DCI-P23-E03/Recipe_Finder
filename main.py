import csv
from add_recipe import add_recipe_to_csv

file_path = '/home/user/Documents/DCI_CODE/assignments2023/Recipe_Finder/RecipeNLG_dataset_smaller.csv'

cookbook_menu = input("""   Welcome to the Recipe Finder!
                            Choose an option (with a number): 
                            \n1. Add a recipe 
                            \n2. Search for a recipe 
                            \n3. Display recipe details
                            \n4. Edit a recipe
                            \n5. Delete a recipe
""")
if cookbook_menu == '1':
    add_recipe_to_csv(file_path)
#elif cookbook_menu == '2':
    #recipe_search(file_path)