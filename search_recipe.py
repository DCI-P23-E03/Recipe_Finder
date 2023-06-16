import csv
import random

def search():
    with open("./RecipeNLG_dataset_smaller.csv") as file:
        reader = csv.reader(file) 

        keyselection = input(""" What are you looking for today? 
        Press [a] if you want to be inspired or put in an ingredient of your choice: \t""") # request user input
        recipe_list = []
        for row in reader:
            if keyselection in row [1] or keyselection in row [2] or keyselection in row [5]:
                recipe_number = row [0]
                recipe_name = row [1]
                recipe_list.append(recipe_number)
                
                print (f"We found the following recipe(s) for you:\n {recipe_number} {recipe_name}")
            #elif keyselection not in row [1] and keyselection not in row [2] and keyselection not in row [5]:
                #print("No recipes matching your search.")
                #break
                        
                    

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
  