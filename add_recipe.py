import csv
def get_last_recipe_number(file_path):
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            recipe_numbers = [int(row[0]) for row in reader if row[0].isdigit()]
        return max(recipe_numbers) if recipe_numbers else 0
    except FileNotFoundError:
        return 0

def add_recipe_to_csv(file_path):
    last_recipe_number = get_last_recipe_number(file_path)
    recipe_number = last_recipe_number + 1

    print(f"Recipe number: {recipe_number}")

    title = input("Enter the recipe title: ")

    # Prompt user for ingredients
    ingredients = []
    ingredient_number = 1
    while True:
        ingredient = input(f"Enter ingredient {ingredient_number}: ")
        if ingredient_number != 1:
            print("(or type 'done' to finish adding ingredients)")
        if ingredient.lower() == 'done':
            break
        ingredients.append(ingredient)
        print(f"Ingredient {ingredient_number}: {ingredient}")
        ingredient_number += 1

    # Prompt user for directions
    directions = []
    direction_number = 1
    while True:
        direction = input(f"Enter direction {direction_number}: ")
        if direction_number != 1:
            print("(or type 'done' to finish adding directions)")
        if direction.lower() == 'done':
            break
        directions.append(direction)
        print(f"Direction {direction_number}: {direction}")
        direction_number += 1

    # Prompt user for keywords
    keywords = []
    keyword_number = 1
    while True:
        keyword = input(f"Enter keyword {keyword_number}: ")
        if keyword_number != 1:
            print("(or type 'done' to finish adding keywords)")
        if keyword.lower() == 'done':
            break
        keywords.append(keyword)
        print(f"Keyword {keyword_number}: {keyword}")
        keyword_number += 1

    link = input("Enter the recipe link: ")
    source = input("Enter the recipe source (or 's' to skip): ")
    if source.lower() == 's':
        source = '---'



    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([recipe_number, title, f'["{", ".join(ingredients)}"]', f'["{", ".join(directions)}"]', link, source, f'["{", ".join(keywords)}"]'])


    # Print the added recipe
    print("The recipe you added:")
    print(f"Title: {title}")
    print("Ingredients:")
    for i, ingredient in enumerate(ingredients, start=1):
        print(f"{i}. {ingredient}")
    print("\nDirections:")
    for i, direction in enumerate(directions, start=1):
        print(f"{i}. {direction}")
    print("\nLink to the recipe:")
    print(link)
    if source != "s":
        print("Source: " + (source))# if source else "No source"))
    print("Keywords: " + ', '.join(keywords))
