import csv
from add_recipe import add_recipe_to_csv
from search_recipe import recipe_search
from display_recipe import display
from search_to_edit import search_edit, justedit
from delete_recipe import delete_recipe
from bookTools import clear_screen, file_path


#file_path = '/home/user/Documents/DCI_CODE/assignments2023/RecipeNLG_dataset_smaller.csv'

cookbook_menu = input("""   Welcome to the Recipe Finder!
                            Choose an option (with a number): 
                            
                            \n1. Search for a recipe 
                            \n2. Display all recipes 
                            \n3. Edit a recipe
                            \n4. Add a recipe
                            \n5. Delete a recipe
                            \n

""")
if cookbook_menu == '1':
    search_edit()
elif cookbook_menu == '2':
    display(file_path)
elif cookbook_menu == '3':  
    justedit()
elif cookbook_menu == '4':
    add_recipe_to_csv(file_path)
elif cookbook_menu == '5':
    delete_recipe(file_path)
else:
    print("Please choose a valid option")
