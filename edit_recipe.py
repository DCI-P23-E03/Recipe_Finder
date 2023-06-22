import csv
import ast
import os
from bookTools import clear_screen, file_path

# Call the function to clear the screen
#clear_screen()

def print_recipe (recipe):
    clear_screen()
    print('EDIT RECIPE:\n')
    print('[1] TITLE:', recipe[1], '\n')
    print('[2] INGREDIENTS:')
    list_of_ingredients = ast.literal_eval(recipe[2])
    for ing in list_of_ingredients:
        print(ing)
    print('\n[3] DIRECTIONS:')
    list_of_instructions = ast.literal_eval(recipe[3])
    for ins in list_of_instructions:
        print(ins)
    print('\n[4] LINK:')
    print(recipe[4])
    print('\n[5] SOURCE:')
    print(recipe[5])
    print('\n[6] KEYWORDS:')
    list_of_ner = ast.literal_eval(recipe[6])
    for ner in list_of_ner:
        print(ner)
    return

def update_values(values_in):

    values_out = values_in

    sel = ''
    while sel not in ['Q', 'S', 'q', 's']:

        print_recipe(values_out)
        sel = input('\nSELECT A SECTION TO UPDATE[1-6], "S" SAVE CHANGES, "Q" TO CANCEL UPDATE:')

        if sel not in ['1','2','3','4','5','6','S','Q','s','q']:
            input('Option not valid. Press ENTER to continue...')

        elif sel == '1':
            clear_screen()
            print('[1] TITLE:', values_out[1])
            val = input('Enter new value, or just ENTER to skip update:')
            if val != '':
                values_out[1] = val

        elif sel == '2': #update ingredients
            lin = ' '
            list_of_ingredients = ast.literal_eval(values_out[2])
            while lin != '':
                clear_screen()
                print('[2] INGREDIENTS:')

                opt = 'a'
                for ing in list_of_ingredients:
                    print(opt,'-',ing)
                    opt = chr(ord(opt)+1) #creates a list of dinamic values for the user
                lin = input('\nChoose a line to update, or ENTER to finish:')
                if lin !='':
                    if ord(lin) >= ord('a') and ord(lin) < ord(opt):
                        print(list_of_ingredients[ord(lin)-ord('a')])
                        val = input('Enter new value, or just ENTER to skip update:')
                        if val != '':
                            list_of_ingredients[ord(lin)-ord('a')] = val
            
                values_out[2] = "[" + ", ".join(['"' + s + '"' for s in list_of_ingredients]) + "]" #convert list back into a string

        elif sel == '3': #update instructions
            lin = ' '
            list_of_instructions = ast.literal_eval(values_out[3])
            while lin != '':
                clear_screen()
                print('[3] DIRECTIONS:')

                opt = 'a'
                for ing in list_of_instructions:
                    print(opt,'-',ing)
                    opt = chr(ord(opt)+1) #creates a list of dinamic values for the user
                lin = input('\nChoose a line to update, or ENTER to finish:')
                if lin !='':
                    if ord(lin) >= ord('a') and ord(lin) < ord(opt):
                        print(list_of_instructions[ord(lin)-ord('a')])
                        val = input('Enter new value, or just ENTER to skip update:')
                        if val != '':
                            list_of_instructions[ord(lin)-ord('a')] = val
                
                values_out[3] = "[" + ", ".join(['"' + s + '"' for s in list_of_instructions]) + "]" #convert list back into a string

        elif sel == '4':
            clear_screen()
            print('[4] LINK:', values_out[4])
            val = input('Enter new value, or just ENTER to skip update:')
            if val != '':
                values_out[4] = val

        elif sel == '5':
            clear_screen()
            print('[5] SOURCE:', values_out[5]) 
            val = input('Enter new value, or just ENTER to skip update:')
            if val != '':
                values_out[5] = val

        elif sel == '6': #update NER
            lin = ' '
            list_of_ner = ast.literal_eval(values_out[6])
            while lin != '':
                clear_screen()
                print('[6] KEYWORDS:')

                opt = 'a'
                for ing in list_of_ner:
                    print(opt,'-',ing)
                    opt = chr(ord(opt)+1) #creates a list of dinamic values for the user
                lin = input('\nChoose a line to update, or ENTER to finish:')
                if lin !='':
                    if ord(lin) >= ord('a') and ord(lin) < ord(opt):
                        print(list_of_ner[ord(lin)-ord('a')])
                        val = input('Enter new value, or just ENTER to skip update:')
                        if val != '':
                            list_of_ner[ord(lin)-ord('a')] = val
                            
                values_out[6] = "[" + ", ".join(['"' + s + '"' for s in list_of_ner]) + "]" #convert list back into a string

        if sel in ['Q', 'q']: #if update is aborted, return original values
            values_out = values_in 

    return values_out

def update_recipe(row_index):

    global file_path

    csv_file = file_path #update file path

    with open(csv_file, 'r') as file: #open file for reading
        # Create a CSV reader object
        reader_obj = csv.reader(file)
        rows = list(reader_obj) # Read all the rows into a list

    idx_upt = row_index -1  #+ 1 #correct row number considering column headers

    rows[idx_upt] = update_values(rows[idx_upt])

    # Rewrite the CSV file with the updated record
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    return

#test
#file_path = 'RecipeNLG_dataset_smaller.csv'
#edit_recipe(file_path, 0)