import csv
import random

def search():
    with open("./RecipeNLG_dataset_smaller.csv") as file:
        reader = csv.reader(file) 

        keyselection = input(""" What are you looking for today? 
        Press [a] if you want to be inspired or put in an ingredient of your choice: \t""") # request user input

        for row in reader:
            if keyselection in row [1] or keyselection in row [2] or keyselection in row [5]:
                recipe_number = row [0]
                print (f"We found the following recipe(s) for you {recipe_number} {row [0]}")    
            elif keyselection not in row[1] and keyselection not in row [2] or keyselection not in row [5]:
                print ("No recipes matching your search.")        
            if keyselection == "a":
                random_recipe = random.choice(row)
                print (random_recipe[1])
                    

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
  