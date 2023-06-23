import csv 

file_path = 'RecipeNLG_dataset_smaller.csv'

#open csv file
file = csv.reader(open(file_path, 'r'))

#create a dictionary
recipe_dict = {}

#loop through the csv file and add the data to the dictionary {title: {ingredients : ingredients, directions : directions, link : link, keywords : NER}}
for row in file:
    recipe_dict[row[1]] = {"ingredients": row[2], "link": row[4], "keywords": row[6]}

#drop first key and value from dictionary
recipe_dict.pop("title", None)

###################################################################################################################################################################################################


def search_recipe():

    #create menu for user to choose from
    search_menu = input("""   How would you like to search for a recipe?
                            Choose an option (with a number): 
                            \n1. Search by ingredient
                            \n2. Search by title
    """)

    #if user chooses option 1, run search_by_ingredient function
    if search_menu == "1":

        #ask user for input for recipe ingredient
        recipe_keyword = input("What ingredients are you looking for? ").upper()

        #search for a recipe by ingredient
        x = 0
        for key in recipe_dict:
            if recipe_keyword in recipe_dict[key]["ingredients"].upper():
                x += 1
                print("##############################################################################################################")
                print("\n")
                print(key)
                print("\n")                
                print("INGREDIENTS: ", recipe_dict[key]["ingredients"][1:-1].replace('"',''))
                print("\n")
                print("LINK: ", recipe_dict[key]["link"])
                print("\n")
                print("KEYWORDS: ", recipe_dict[key]["keywords"][1:-1].replace('"',''))
                print("\n")
                print("##############################################################################################################")
                print("\n")
                return x
        if x == 0:
            print("\n")
            print(f"No match with {recipe_keyword} found :(")
            print("\n")
                

    #if user chooses option 2, run search_by_title function
    if search_menu == "2":
        
        #ask user for input for recipe title
        recipe_keyword = input("What title are you looking for? ").upper()

        #search for a recipe by title
        x = 0
        for key in recipe_dict:
            if recipe_keyword in key.upper():
                x += 1
                print("##############################################################################################################")
                print("\n")
                print(key)
                print("\n")                
                print("INGREDIENTS: ", recipe_dict[key]["ingredients"][1:-1].replace('"',''))
                print("\n")
                print("LINK: ", recipe_dict[key]["link"])
                print("\n")
                print("KEYWORDS: ", recipe_dict[key]["keywords"][1:-1].replace('"',''))
                print("\n")
                return x
        if x == 0:
            print("\n")
            print(f"No match with {recipe_keyword} found :(")
            print("\n")
                

##################################################################################################################################################################################################


#defining a function to add a recipe
def add_recipe():
    #ask user for input for recipe title
    recipe_title = input("What is the title of your recipe? ")
    #ask user for input for recipe ingredients
    recipe_ingredients = input("What are the ingredients of your recipe? ")
    #ask user for input for recipe link
    recipe_link = input("What is the link of your recipe? ")
    #ask user for input for recipe keywords
    recipe_keywords = input("What are the keywords of your recipe? ")
    #add recipe to dictionary
    recipe_dict[recipe_title] = {"ingredients": f"{recipe_ingredients}", "link": recipe_link, "keywords": [f"{recipe_keywords}"]}  
    #print recipe dictionary
    print("\n")
    print("##############################################################################################################")
    print("\n")
    print(recipe_title)
    print("\n")                
    print("INGREDIENTS: ", recipe_ingredients)
    print("\n")
    print("LINK: ", recipe_link)
    print("\n")
    print("KEYWORDS: ", recipe_keywords)
    print("\n")
    print("##############################################################################################################")
    print("\n")



###################################################################################################################################################################################################

#defining a function to edit a recipe
def edit_recipe():
    #ask user for input for recipe title
    recipe_title = input("What is the title of your recipe? ")
    #ask user for input for recipe ingredients
    recipe_ingredients = input("What are the ingredients of your recipe? ")
    #ask user for input for recipe link
    recipe_link = input("What is the link of your recipe? ")
    #ask user for input for recipe keywords
    recipe_keywords = input("What is the keyword of your recipe? ")
    #add recipe to dictionary
    recipe_dict[recipe_title] = {"ingredients": f"{recipe_ingredients}", "link": recipe_link, "keywords": [f"{recipe_keywords}"]}  
    #print recipe dictionary
    print("\n")
    print("##############################################################################################################")
    print("\n")
    print(recipe_title)
    print("\n")                
    print("INGREDIENTS: ", recipe_ingredients)
    print("\n")
    print("LINK: ", recipe_link)
    print("\n")
    print("KEYWORDS: ", recipe_keywords)
    print("\n")
    print("##############################################################################################################")
    print("\n")


###################################################################################################################################################################################################

#defining a function to delete a recipe
def delete_recipe():
    #ask user for input for recipe title
    recipe_title = input("What is the title of your recipe? ")
    #delete recipe from dictionary
    recipe_dict.pop(recipe_title, None)
    #print recipe dictionary
    print("\n")
    print("##############################################################################################################")
    print("\n")
    print(f"{recipe_title} deleted :)")
    print("\n")
    print("##############################################################################################################")
    print("\n")

###################################################################################################################################################################################################

# while loop to keep the program running until the user chooses Escape to exit
while True:
    #create menu for user to choose from
    menu = input("""   What would you like to do?
                    Choose an option (with a number): 
                    \n1. Search for a recipe
                    \n2. Add a recipe
                    \n3. Edit a recipe
                    \n4. Delete a recipe
                    \n5. Exit
    """)
    #if user chooses option 1, run search_recipe function
    if menu == "1":
        search_recipe()
    #if user chooses option 2, run add_recipe function
    elif menu == "2":
        add_recipe()
    #if user chooses option 3, run edit_recipe function
    elif menu == "3":
        edit_recipe()
    #if user chooses option 4, run delete_recipe function
    elif menu == "4":
        delete_recipe()
    #if user chooses option 5, exit the program
    elif menu == "5":
        print("Goodbye!")
        break
    #if user chooses an option that is not on the menu, print error message
    else:
        print("That is not an option. Please choose an option from the menu.")