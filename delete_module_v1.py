import pandas as p
from bookTools import file_path

def delete_d(recipe):

    index = recipe ### connect with search to get indexes

    # read file and get names of recipes (https://www.w3schools.com/python/pandas/pandas_csv.asp)
    df = p.read_csv(file_path)  
    name = df.loc[index, 'title']  ##https://www.geeksforgeeks.org/python-pandas-dataframe-loc/
    print('Is this the recipe you want to delete?')
    print(name)
    #for k, name in enumerate(names):
    # print(f'{k+1}. {name}')

    # user's choice what to delete
    to_del = input('Press Y(es) if you want to delete')
    if to_del == 'y':
        df.drop(recipe, inplace=True) #DELELE WITH DELETE IN ORIGINAL
        df.to_csv(file_path, index=False)
        print('Chosen recipe(s) are deleted')

    # row delete and save changes into the file
    

    

#delete_d()
## УДАЛЕНИЕ СПИСКА
## connect with search to get indexes