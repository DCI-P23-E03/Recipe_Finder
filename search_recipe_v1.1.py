import csv
import random
from  edit_recipe import clear_screen

def search():
    with open("/home/dci-student/projects/PythonExcercises/RecipeNLG_dataset_smaller.csv") as file:
        reader = csv.reader(file) 

        keyselection = input(""" What are you looking for today? 
        Please put in an ingredient of your choice: \t""") # request user input
        recipe_list_num = []
        recipe_list_name = []
        recipe_count = 0
  
        for row in reader:
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
            
            opt = 1 # pr
            for recipe in recipe_list_name:
                    print('[',opt,']',recipe)
                    opt = int(opt+1) #creates a list of dynamic values for the user to pick from

            print ("Please choose a recipe you would like to display.")
        else:
            print("No recipes found matching your search.")


       
                        
                    

search()  

     
#def search():# define search function to find recipes
    
    #preference = input("""Welcome to the search.
    #Firstly do you have any dietary preferences or restrictions?
    #[1] vegetarian
    #[2] None"""\n)

    
    
    #if preference == 1:
        #if keyselection == a:
            #random.choice(file) # give out title of random recipe
            #print(title)
    #elif preference == 2:
        #print("2")
        #if keyselection == a:
            #random.choice(file) # give out title of random recipe
            #print(title)
        #elif keyselection in file("title") or keyselection in file ("ingedients") or keyselection in file ("NER")
        #print () 
                  
    #else:
        #print("Please define your preference.") 
    
    
#search()
  