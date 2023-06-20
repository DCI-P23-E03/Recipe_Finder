import csv
import random
from  edit_recipe import clear_screen

def recipe_search():
    with open("/home/dci-student/projects/PythonExcercises/RecipeNLG_dataset_smaller.csv") as file:
        reader = csv.reader(file) 

        keyselection = input(""" What are you looking for today? 
        Please put in an ingredient of your choice: \t""") # request user input
        recipe_list_num = [] 
        recipe_list_name = []
        recipe_count = 0
        recipe_num = int()
    
  
        for row in reader:
            # looking for the keyword in different varieties
            if keyselection in row [1] or keyselection in row [2] or keyselection in row [5]or keyselection.lower() in row [1] or keyselection.lower() in row [2] or keyselection.lower() in row [5] or keyselection.capitalize() in row [1] or keyselection.capitalize() in row [2] or keyselection.capitalize() in row [5]:
                recipe_number = row [0]
                recipe_name = row [1]
                recipe_list_num.append(recipe_number) # Collect recipe numbers in a list to count
                recipe_list_name.append(recipe_name) 
                recipe_count = (len(recipe_list_num))
                #print(type(recipe_count))    
                #print(f"{recipe_number} {recipe_name}")

        clear_screen()

        if recipe_count > 0:
                                
            print(f"We found {recipe_count} recipe(s) that match your search.\nThey are:\n")
            
            opt = 0 # pr
            for recipe in recipe_list_name:
                    print('[',opt,']',recipe)
                    opt += 1 #creates a list of dynamic values for the user to pick from

            # print(recipe_list_num) Check list

            flag = False
            while flag == False:
                choice = input("Please choose a recipe:\t")
                try: 
                    recipe_num = recipe_list_num[int(choice)] # Ensure user's choice is valid
                    flag = True     
                except IndexError:
                    print("Please select a recipe from the list.")
                      

        else:
            print("No recipes found matching your search.")
       
    return recipe_num
       
                        
                    

recipe_search()  

     

  