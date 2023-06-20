import csv 

recipe_dict = {}
def search_recipe():
    #ask user for input for recipe keyword
    display_search = input("""Where are you looking for a recipe?: ")
    \nChoose an option (with a number):
    \n1. Search by title
    \n2. Search by ingredient
    \n3. Search by keyword
    """)

    if display_search == '1':
        recipe_keyword = input("What recipe are you looking for (by title)? ")
        for key in recipe_dict:
            if recipe_keyword.upper() in key.upper():
                print(key, recipe_dict[key])
                print("\n")
            

    
    elif display_search == '2':
        recipe_keyword = input("What recipe are you looking for? (by ingredients) ").upper()
        for key in recipe_dict:
            if recipe_keyword in recipe_dict[key]["ingredients"].upper():
                print(key, recipe_dict[key])
                print("\n")

    elif display_search == '3':
        recipe_keyword = input("What recipe are you looking for? (by keywords) ").upper()
        for keyword, valueword in recipe_dict.items():
            if recipe_keyword in recipe_dict[keyword]["keywords"].upper():
                print(keyword)
            for key,value in valueword.items():
                print(f"{key}: {value}")
                #print(key, recipe_dict[key])
                #print("\n")

    else:
        print("Please choose a valid option")
        search_recipe()

def display(file_path):
    file = csv.reader(open(file_path, 'r'))
    for row in file:
        recipe_dict[row[1]] = {"ingredients": row[2], "link": row[4], "keywords": row[6]}
    recipe_dict.pop("title", None)
    search_recipe()
    
   
