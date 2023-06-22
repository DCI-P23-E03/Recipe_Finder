from search_recipe import recipe_search
from edit_recipe import update_recipe, print_recipe
from bookTools import clear_screen, file_path
from delete_module_v1 import delete_d
import csv

def search_edit():

    selected_row = recipe_search() 

    print('OPTIONS:')
    print('1. Display')
    print('2. Edit')
    print('3. Delete')

    option = input('What would you like to do?      ')

    if option == '1':
        with open(file_path, 'r') as file: #open file for reading
            # Create a CSV reader object
            reader_obj = csv.reader(file)
            rows = list(reader_obj) # Read all the rows into a list

        print_recipe(rows[selected_row-1])

    elif option == '2':
        update_recipe(selected_row)
    elif option == '3':
        delete_d(selected_row-2) #delete
    else:
        print('Please select a valid option.')


    return 

def justedit():
    selected_row = recipe_search() 
    update_recipe(selected_row)