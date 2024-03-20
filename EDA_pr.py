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
    columns = columns[1:] # skip the first index
    print("THE MINIMUM AND MAXIMUM HOUSE PRICES FOR EACH NEIGHBORHOOD AND THE DATES FOR WHEN THESE PRICES OCCURED", end= "\n\n")
    map = {}
    min_price_list = []
    max_price_list = []
    min_date_list = []
    max_date_list = []
    
    for column in columns:
        min_date = data.loc[data[column] == data[column].min(), 'date'].iloc[0]
        max_date = data.loc[data[column] == data[column].max(), 'date'].iloc[0]
        min_price_list.append(data[column].min())
        min_date_list.append(min_date)
        max_price_list.append(data[column].max())
        max_date_list.append(max_date)

    map['Neighborhood'] = columns
    map['Min Price'] = min_price_list
    map['Min Date'] = min_date_list
    map['Max Price'] = max_price_list
    map['Max Date'] = max_date_list

    df = pd.DataFrame(map)
    # df['Min Price'] = df['Min Price'].astype(float)
    # df['Max Price'] = df['Max Price'].astype(float)

    pd.set_option("display.max_rows", None)

    # get the min, max, range, average price for all neighborhoods and their specifications
    print(df.iloc[:,:], end = "\n\n")
    
    # get the avg min price, avg max price for all neighborhoods and their specifications
    print("AVG MIN PRICE: ", df['Min Price'].mean(), "  AVG MAX PRICE: ", df['Max Price'].mean(), end="\n\n")

    # get median min price, median max price for all neighborhoods and their specifications
    print("MEDIAN MIN PRICE: ", df['Min Price'].median(), "  MEDIAN MAX PRICE: ", df['Max Price'].median(), end="\n\n")

    # Most Cheap Neighborhood amongs the min price houses in each neighborhood
    row1 = df.loc[df['Min Price'] == df['Min Price'].min(), ['Neighborhood', 'Min Price', 'Min Date']].iloc[0]

    # Most Expensive Neighborhood amongs the max price houses in each neighborhood
    row2 = df.loc[df['Max Price'] == df['Max Price'].max(), ['Neighborhood', 'Max Price', 'Max Date']].iloc[0]

    print("Least Expensive Neighborhood: ",row1.iloc[0], ' $',row1.iloc[1], ' ',row1.iloc[2], end="\n\n", sep='')

    print("Most Expensive Neighborhood: ",row2.iloc[0], ' $',row2.iloc[1], ' ',row2.iloc[2], end="\n\n", sep ='')

    

def main():
    neighborhood_2017_2019 = pd.read_csv('csv_files/neighborhood_data_2017_2019.csv')
    neighborhood_2021_present = pd.read_csv('csv_files/neighborhood_data_2021_present.csv')

    print("HOUSE PRICE BETWEEN 2017-19")
    get_neighborhood_price_stats(neighborhood_2017_2019)
    print("~"*160)
    print("HOUSE PRICE BETWEEN 2021-present")
    get_neighborhood_price_stats(neighborhood_2021_present)

if __name__ == "__main__":
    main()