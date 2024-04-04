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

def neighborhood_parse_df(data:pd.DataFrame):
    columns = data.columns.to_list()
    columns = columns[1:] # skip the first index
    print("THE MINIMUM AND MAXIMUM HOUSE PRICES FOR EACH NEIGHBORHOOD AND THE DATES FOR WHEN THESE PRICES OCCURED", end= "\n\n")
    map = {}
    map2 = {}
    min_price_list = []
    max_price_list = []
    min_date_list = []
    max_date_list = []
    avg_price_list = []
    median_price_list = []
    
    for column in columns:
        min_date = data.loc[data[column] == data[column].min(), 'date'].to_list()[0]
        max_date = data.loc[data[column] == data[column].max(), 'date'].to_list()[0]
        min_price_list.append(data[column].min())
        min_date_list.append(min_date)
        max_price_list.append(data[column].max())
        max_date_list.append(max_date)
        avg_price_list.append(data[column].mean())
        median_price_list.append(data[column].median())

    map['Neighborhood'] = columns
    map['Min Price'] = min_price_list
    map['Min Date'] = min_date_list
    map['Max Price'] = max_price_list
    map['Max Date'] = max_date_list

    map2['Neighborhood'] = columns
    map2['Avg Price'] = avg_price_list
    map2['Med Price'] = median_price_list

    df = pd.DataFrame(map)
    df2 = pd.DataFrame(map2)

    df['Min Date'] = pd.to_datetime(df['Min Date'])
    df['Max Date'] = pd.to_datetime(df['Max Date'])

    return df, df2

def neighborhood_min_max(df:pd.DataFrame):
    # pd.set_option("display.max_rows", None)

    print(df.to_string(index=False), end = "\n\n")

def get_neighborhood_price_stats(data:pd.DataFrame):
    '''This function will calculate the max, min, average'''

    columns = data.columns.to_list()
    columns = columns[1:] # skip the first index
    # print("\nTHE MINIMUM AND MAXIMUM HOUSE PRICES FOR EACH NEIGHBORHOOD AND THE DATES FOR WHEN THESE PRICES OCCURED", end= "\n\n")
    map = {}
    map2 = {}
    min_price_list = []
    max_price_list = []
    min_date_list = []
    max_date_list = []
    avg_price_list = []
    median_price_list = []
    
    for column in columns:
        min_date = data.loc[data[column] == data[column].min(), 'date'].to_list()[0]
        max_date = data.loc[data[column] == data[column].max(), 'date'].to_list()[0]
        min_price_list.append(data[column].min())
        min_date_list.append(min_date)
        max_price_list.append(data[column].max())
        max_date_list.append(max_date)
        avg_price_list.append(data[column].mean())
        median_price_list.append(data[column].median())

    map['Neighborhood'] = columns
    map['Min Price'] = min_price_list
    map['Min Date'] = min_date_list
    map['Max Price'] = max_price_list
    map['Max Date'] = max_date_list

    map2['Neighborhood'] = columns
    map2['Avg Price'] = avg_price_list
    map2['Med Price'] = median_price_list

    df = pd.DataFrame(map)
    df2 = pd.DataFrame(map2)

    df['Min Date'] = pd.to_datetime(df['Min Date'])
    df['Max Date'] = pd.to_datetime(df['Max Date'])

    # get the avg min price, avg max price for all neighborhoods and their specifications
    print("AVG MIN PRICE: ", round(df['Min Price'].mean(),2), "  AVG MAX PRICE: ", round(df['Max Price'].mean(),2), end="\n")

    # get median min price, median max price for all neighborhoods and their specifications
    print("MEDIAN MIN PRICE: ", round(df['Min Price'].median(),2), "  MEDIAN MAX PRICE: ", round(df['Max Price'].median(),2), end="\n")

    # Most Cheap Neighborhood amongs the min price houses in each neighborhood
    row1 = df.loc[df['Min Price'] == df['Min Price'].min(), ['Neighborhood', 'Min Price', 'Min Date']].iloc[0]

    # Most Expensive Neighborhood amongs the max price houses in each neighborhood
    row2 = df.loc[df['Max Price'] == df['Max Price'].max(), ['Neighborhood', 'Max Price', 'Max Date']].iloc[0]

    print("Cheapest House Price: ",row1.iloc[0], ' $',row1.iloc[1], ' ',row1.iloc[2].date().strftime("%Y-%m-%d"), end="\n", sep='')

    print("Expensive House Price: ",row2.iloc[0], ' $',row2.iloc[1], ' ',row2.iloc[2].date().strftime("%Y-%m-%d"), end="\n", sep ='')

    avg_Min = df2.loc[df2['Avg Price'] == df2['Avg Price'].min(), ['Neighborhood', 'Avg Price']].iloc[0]
    avg_Max = df2.loc[df2['Avg Price'] == df2['Avg Price'].max(), ['Neighborhood', 'Avg Price']].iloc[0]

    med_min = df2.loc[df2['Med Price'] == df2['Med Price'].min(), ['Neighborhood', 'Med Price']].iloc[0]
    med_max = df2.loc[df2['Med Price'] == df2['Med Price'].max(), ['Neighborhood', 'Med Price']].iloc[0]
    
    print('USING AVERAGE')
    print("\tCheapest Neighborhood: ", avg_Min.iloc[0], ' $',avg_Min.iloc[1].round(2), end="\n", sep='')
    print("\tExpensive Neighborhood: ", avg_Max.iloc[0], ' $',avg_Max.iloc[1].round(2), end="\n", sep='')


    print('USING MEDIAN')
    print("\tCheapest Neighborhood: ", med_min.iloc[0], ' $',med_min.iloc[1].round(2), end="\n", sep='')
    print("\tExpensive Neighborhood: ", med_max.iloc[0], ' $',med_max.iloc[1].round(2), end="\n", sep='')
    # print(df['Max Date'].info())

def crime_parse_df(data:pd.DataFrame):
    print("Least Common Type of Crime: ",data['Primary Type'].min())
    print("Most Common Type of Crime: ",data['Primary Type'].max(), end="\n\n\n")

    data2 = data[['RegionName', 'Arrest']]

    group_df = (data2.groupby(['RegionName']).sum().reset_index()) # Arrest
    
    group_df_2 = (data2.groupby(['RegionName']).count().reset_index()) # Crime
    group_df_2.rename(columns={'Arrest':'NUM CRIME'}, inplace=True)
    return group_df, group_df_2

def print_neighborhood_crimes(df:pd.DataFrame):
    print("THE NUMBER OF CRIMES FOR EACH NEIGHBORHOOD\n")
    pd.set_option("display.max_rows", None)
    print(df.to_string(index=False), end = "\n\n")

def get_crime_stats(data:pd.DataFrame):
    '''most and least common type of crime'''

    print("Least Common Type of Crime: ",data['Primary Type'].min())
    print("Most Common Type of Crime: ",data['Primary Type'].max(), end="\n\n")

    # neighborhoods with the most and least arrest  # more arrest = active police
    # step 1, group the data

    data2 = data[['RegionName', 'Arrest']]

    group_df = (data2.groupby(['RegionName']).sum().reset_index()) # Arrest
    
    group_df_2 = (data2.groupby(['RegionName']).count().reset_index()) # Crime
    group_df_2.rename(columns={'Arrest':'NUM CRIME'}, inplace=True)

    # print("THE NUMBER OF CRIMES FOR EACH NEIGHBORHOOD\n")
    # pd.set_option("display.max_rows", None)
    # print(group_df_2.to_string(index=False), end = "\n\n")

    least_arrest = group_df[group_df['Arrest']==group_df['Arrest'].min()].iloc[0]
    most_arrest = group_df[group_df['Arrest']==group_df['Arrest'].max()].iloc[0]

    print("Neighborhood with Least Arrest: ", least_arrest.iloc[0], ", Number of Arrest: ", least_arrest.iloc[1])
    print("Neighborhood with Most Arrest: ",most_arrest.iloc[0], ", Number of Arrest: ", most_arrest.iloc[1], end="\n\n")

    # neighborhoods with the most and least crime   # more crime = less safe
    least_crime = group_df_2[group_df_2['NUM CRIME']==group_df_2['NUM CRIME'].min()].iloc[0]
    most_crime = group_df_2[group_df_2['NUM CRIME']==group_df_2['NUM CRIME'].max()].iloc[0]

    print("Neighborhood with Least Crime: ", least_crime.iloc[0], ", Number of Crimes: ", least_crime.iloc[1])
    print("Neighborhood with Most Crime: ",most_crime.iloc[0], ", Number of Crimes: ", most_crime.iloc[1], end="\n\n")
    # most and least common crime location description

    data3 = data[['Location Description', 'ID']]
    data3 = (data3.groupby(['Location Description']).count().reset_index())
    data3.rename(columns={'ID':'NUM CRIME'}, inplace=True)
    print("TOP 5 LOCATION MOST CRIME")
    print(data3.sort_values('NUM CRIME', ascending=False).head(5).to_string(index=False), end="\n\n")

    print("TOP 5 LOCATION LEAST CRIME")
    print(data3.sort_values('NUM CRIME').head(5).to_string(index=False), end = "\n\n")

    # The day with the most crime 
    data['New_Date'] = pd.to_datetime(data['New_Date'])
    # print(data.head())
    data4 = data.copy()
    data4 = data4[['New_Date', 'ID']]
    data4['New_Date'] = data4['New_Date'].apply(lambda x: x.strftime("%B"))
    
    data4 = data4.groupby(['New_Date']).count().reset_index()
    data4.rename(columns={'New_Date':'Month', "ID": 'NUM CRIMES'}, inplace=True)
    print("LIST OF MONTHS WITH NUMBER OF CRIMES FROM MOST TO LEAST", end="\n\n")
    print(data4.sort_values('NUM CRIMES', ascending=False).to_string(index=False), end= "\n\n\n")

    # Use Severity to display most common level of crime in each neighborhood
    # data5 = data[['RegionName', 'Severity_Score']]
    # data5 = data5.groupby('RegionName')['Severity_Score'].agg(lambda x: x.mode()).reset_index()
    # print("MOST COMMON LEVEL OF CRIME IN EACH NEIGHBORHOOD")
    # print(data5.sort_values('Severity_Score', ascending=False).to_string(index=False))


def main():
    neighborhood_2017_2019 = pd.read_csv('csv_files/neighborhood_data_2017_2019.csv')
    neighborhood_2021_present = pd.read_csv('csv_files/neighborhood_data_2021_present.csv')


    print("HOUSE PRICE BETWEEN 2017-19")
    #df, df2 = neighborhood_parse_df(neighborhood_2017_2019)
    # neighborhood_min_max(df)
    get_neighborhood_price_stats(neighborhood_2017_2019)

    print("HOUSE PRICE BETWEEN 2021-present")
   # df3, df4 = neighborhood_parse_df(neighborhood_2021_present)
    # neighborhood_min_max(df)
    get_neighborhood_price_stats(neighborhood_2021_present)

    # print("#"*160)
    crime_data1 = pd.read_csv('csv_files/Crimes_2017_to_2019.csv')
    print("CRIME STATS (2017-19)")
    # g1, g2 = crime_parse_df(crime_data1)
    get_crime_stats(crime_data1)

    # print("~"*160)
    crime_data2= pd.read_csv('csv_files/Crimes_2021_to_Present.csv')
    print("CRIME STATS (2021-Present)")
    get_crime_stats(crime_data2)

if __name__ == "__main__":
    main()