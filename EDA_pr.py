import pandas as pd
import numpy as np

def get_max(col_name, df):
    map = {}
    temp = df[col_name].to_list()
    for i in temp:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1

    max = float('-inf')
    key = ''
    for x, y in map.items():
        if y > max:
            max = y
            key = x
    return key

def get_min(col_name, df):
    map = {}
    temp = df[col_name].to_list()
    for i in temp:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1

    min = float('inf')
    key = ''
    for x, y in map.items():
        if y < min:
            min = y
            key = x
    return key

def get_neighborhood_price_stats(data:pd.DataFrame):
    '''This function will calculate the max, min, average'''
    columns = data.columns.to_list()
    
    print("THE MINIMUM AND MAXIMUM HOUSE PRICES FOR EACH NEIGHBORHOOD AND THE DATES FOR WHEN THESE PRICES OCCURED")
    for column in columns:
        print(column)
        # min_date = data.loc[data[column] == data[column].min(), 'date']
        # max_date = data.loc[data[column] == data[column].max(), 'date']
        # print(column, " Min:", data[column].min(),"Date:", min_date.iloc[0], ", Max:", data[column].max(), "Date:", max_date.iloc[0])


    

def main():
    neighborhood_2017_2019 = pd.read_csv('csv_files/neighborhood_data_2017_2019.csv')
    get_neighborhood_price_stats(neighborhood_2017_2019)

if __name__ == "__main__":
    main()