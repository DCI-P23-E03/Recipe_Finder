import pandas as p
from bookTools import file_path

def delete_d(recipe):

    index = recipe ### connect with search to get indexes

    # read file and get names of recipes (https://www.w3schools.com/python/pandas/pandas_csv.asp)
    df = p.read_csv(file_path)  
    name = df.loc[index, 'title']  ##https://www.geeksforgeeks.org/python-pandas-dataframe-loc/
    print('Is this the recipe you want to delete?\n')
    print(name)
    #for k, name in enumerate(names):
    # print(f'{k+1}. {name}')
    # user's choice what to delete
    to_del = input('\nPress Y if you want to delete:\t')
    if to_del == 'y' or to_del.upper() == 'Y':
        df.drop(recipe, inplace=True) #DELETE WITH DELETE IN ORIGINAL
        df.to_csv(file_path, index=False)
        print('\nThe recipe you chose has been deleted.')
    else:
        print("\nCancelled. Nothing deleted.")    

    # row delete and save changes into the file
    return    

    

#delete_d()
## УДАЛЕНИЕ СПИСКА
## connect with search to get indexes