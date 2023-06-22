import pandas as p

def delete_d():

    indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8] ### connect with search to get indexes

    # read file and get names of recipes (https://www.w3schools.com/python/pandas/pandas_csv.asp)
    df = p.read_csv('RecipeNLG_dataset_smaller.csv')  
    names = df.loc[indexes, 'title']  ##https://www.geeksforgeeks.org/python-pandas-dataframe-loc/
    print('List of recipes:')
    for k, name in enumerate(names):
        print(f'{k+1}. {name}')

    # user's choice what to delete
    to_del = int(input('Enter prescription number to delete: '))

    # get index to delete
    index_to_delete = indexes[to_del - 1] 

    # row delete and save changes into the file
    df.drop(index_to_delete, inplace=True) #DELELE WITH DELETE IN ORIGINAL
    df.to_csv('RecipeNLG_dataset_smaller.csv', index=False)

    print('Chosen recipe(s) are deleted')

delete_d()
## УДАЛЕНИЕ СПИСКА
## connect with search to get indexes