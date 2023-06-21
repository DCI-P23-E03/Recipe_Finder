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
    #ask user for input for recipe keyword
    recipe_keyword = input("What recipe are you looking for? ").upper()

    #search for a recipe by ingredient flour
    for key in recipe_dict:
        if recipe_keyword in recipe_dict[key]["ingredients"].upper():
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
    print(recipe_dict[recipe_title])

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

#create a menu for the user to choose from

cookbook_menu = input("""   Welcome to the Recipe Finder!
                            Choose an option (with a number): 
                            \n1. Add a recipe 
                            \n2. Search for a recipe by keyword
                            \n3. Edit a recipe
                            \n4. Delete a recipe
""")
                      
if cookbook_menu == '1':
    add_recipe()
elif cookbook_menu == '2':
    search_recipe()
elif cookbook_menu == '3':
    edit_recipe()
elif cookbook_menu == '4':
    delete_recipe()
else:
    print("Please enter a valid option")