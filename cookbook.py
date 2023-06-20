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

    #ask user for input for recipe keyword
    recipe_keyword = input("What recipe are you looking for? ").upper()

    #search for a recipe by ingredient
    for key in recipe_dict:
        if recipe_keyword in recipe_dict[key]["ingredients"].upper():
            print(key, recipe_dict[key])
            print("\n") 

    #search for a recipe by title
    for key in recipe_dict:
        if recipe_keyword in key.upper():
            print(key, recipe_dict[key])
            print("\n")

###################################################################################################################################################################################################


#defining a function to add a recipe
def add_recipe():
    #ask user for input for recipe title
    recipe_title = input("What is the title of your recipe? ")

    #ask user for input for recipe ingredients
    recipe_ingredients = input("What are the ingredients of your recipe? ")

    #ask user for input for recipe directions
    recipe_directions = input("What are the directions of your recipe? ")

    #ask user for input for recipe link
    recipe_link = input("What is the link of your recipe? ")

    #ask user for input for recipe keywords
    recipe_keywords = input("What are the keywords of your recipe? ")

    #add recipe to dictionary
    recipe_dict[recipe_title] = {"ingredients": recipe_ingredients, "directions": recipe_directions, "link": recipe_link, "keywords": recipe_keywords}

    #print recipe dictionary
    print(recipe_title + recipe_dict[recipe_title])

###################################################################################################################################################################################################

#defining a function to edit a recipe
def edit_recipe():
    #ask user for input for recipe title
    recipe_title = input("What is the title of your recipe? ")

    #ask user for input for recipe ingredients
    recipe_ingredients = input("What are the ingredients of your recipe? ")

    #ask user for input for recipe directions
    recipe_directions = input("What are the directions of your recipe? ")

    #ask user for input for recipe link
    recipe_link = input("What is the link of your recipe? ")

    #ask user for input for recipe keywords
    recipe_keywords = input("What is the keyword of your recipe? ")

    #add recipe to dictionary
    recipe_dict[recipe_title] = {"ingredients": recipe_ingredients, "directions": recipe_directions, "link": recipe_link, "keywords": recipe_keywords}

    #print recipe dictionary
    print(recipe_dict[recipe_title])


###################################################################################################################################################################################################

#defining a function to delete a recipe
def delete_recipe():
    #ask user for input for recipe title
    recipe_title = input("What is the title of your recipe? ")

    #delete recipe from dictionary
    recipe_dict.pop(recipe_title, None)

    #print recipe dictionary
    print(recipe_dict)

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