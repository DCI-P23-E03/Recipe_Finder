import csv

def add_recipe_to_csv(file_path, recipe_number,  title, ingredients, directions, link, source, keywords):
    with open(file_path, 'a', newline='') as csvfile:  # Open the CSV file in append mode
        writer = csv.writer(csvfile)  # Create a writer object to write rows to the CSV file
        writer.writerow([recipe_number ,title, ', '.join(ingredients), ', '.join(directions), link, source, ', '.join(keywords)])
        # Write a new row to the CSV file with the provided data
