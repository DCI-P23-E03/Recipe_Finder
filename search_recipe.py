import csv
from bookTools import clear_screen, file_path

def recipe_search():
    clear_screen() #start with a clear screen
    recipe_index = 0    #default function result if not matches are found
    while recipe_index == 0:
        
        with open (file_path) as file:
            #define lists and variables
            reader = csv.reader(file)
            recipe_list_num = [] #define list variable
            recipe_list_name = []
            recipe_count = 0 # define recipe count variable
            recipe_num = 0
            key_list = []
            

            #Prompt userinput
            print("What are you looking for today?")
            x = 1
            while x == 1:
                keyselection = input("""Please put in an ingredient or title: \t""") 
                if keyselection != "":
                    print("\nEnter another ingredient or press ENTER to see results") # ask for more input
                    key_list.append(keyselection.lower())
                elif keyselection =="": # enter stops the while loop
                    x = 0
            
            #print(key_list)

            if len(key_list) == 1: #only looking for one search term
                keyselection = key_list[0]
                for row in reader:
                    # looking for the keyword in different varieties, 
                    if keyselection in row [1] or keyselection in row [2] or keyselection in row [6]or keyselection.lower() in row [6] or keyselection.lower() in row [2] or keyselection.lower() in row [6] or keyselection.capitalize() in row [1] or keyselection.capitalize() in row [2] or keyselection.capitalize() in row [6]:
                        recipe_number = row [0]
                        recipe_name = row [1]
                        recipe_list_num.append(recipe_number) # Collect recipe numbers in a list to count
                        recipe_list_name.append(recipe_name) #Collect recipe names in a list
                        recipe_count = (len(recipe_list_num)) # Calculate how many recipes have been found
    
            
            elif len(key_list) > 1: # search for multiple elements
                for row in reader:
                    if all(key in row[6] for key in key_list) or all(key in row[2] for key in key_list) or all(key in row[1] for key in key_list):
                        recipe_number = row [0]
                        recipe_name = row [1]
                        recipe_list_num.append(recipe_number) # Collect recipe numbers in a list to count
                        recipe_list_name.append(recipe_name) #Collect recipe names in a list
                        recipe_count = (len(recipe_list_num)) # Calculate how many recipes have been found
                    
            clear_screen()

            if recipe_count > 0:
                clear_screen()                    
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
                print("No recipes found matching your search. Try a different search term.\n")
                

            with open("RecipeNLG_dataset_smaller.csv") as file:
                reader = csv.reader(file)
                for row in reader: # try to read out line number
                    if row[0] == recipe_num:
                        recipe_index = reader.line_num
                        #print(recipe_index) 

    return recipe_index # give out recipe index to pass to delete function
       
                                 
#recipe_search()   #this is for test  

     

  