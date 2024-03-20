import pandas as pd
import numpy as np

community_areas = {
        1: "Rogers Park",
        2: "West Ridge",
        3: "Uptown",
        4: "Lincoln Square",
        5: "North Center",
        6: "Lake View",
        7: "Lincoln Park",
        8: "Near North Side",
        9: "Edison Park",
        10: "Norwood Park",
        11: "Jefferson Park",
        12: "Forest Glen",
        13: "North Park",
        14: "Albany Park",
        15: "Portage Park",
        16: "Irving Park",
        17: "Dunning",
        18: "Montclare",
        19: "Belmont Cragin",
        20: "Hermosa",
        21: "Avondale",
        22: "Logan Square",
        23: "Humboldt Park",
        24: "West Town",
        25: "Austin",
        26: "West Garfield Park",
        27: "East Garfield Park",
        28: "Near West Side",
        29: "North Lawndale",
        30: "South Lawndale",
        31: "Lower West Side",
        32: "Loop",
        33: "Near South Side",
        34: "Armour Square",
        35: "Douglas",
        36: "Oakland",
        37: "Fuller Park",
        38: "Grand Boulevard",
        39: "Kenwood",
        40: "Washington Park",
        41: "Hyde Park",
        42: "Woodlawn",
        43: "South Shore",
        44: "Chatham",
        45: "Avalon Park",
        46: "South Chicago",
        47: "Burnside",
        48: "Calumet Heights",
        49: "Roseland",
        50: "Pullman",
        51: "South Deering",
        52: "East Side",
        53: "West Pullman",
        54: "Riverdale",
        55: "Hegewisch",
        56: "Garfield Ridge",
        57: "Archer Heights",
        58: "Brighton Park",
        59: "McKinley Park",
        60: "Bridgeport",
        61: "New City",
        62: "West Elsdon",
        63: "Gage Park",
        64: "Clearing",
        65: "West Lawn",
        66: "Chicago Lawn",
        67: "West Englewood",
        68: "Englewood",
        69: "Greater Grand Crossing",
        70: "Ashburn",
        71: "Auburn Gresham",
        72: "Beverly",
        73: "Washington Heights",
        74: "Mount Greenwood",
        75: "Morgan Park",
        76: "O'Hare",
        77: "Edgewater"
    }
severity_scores = {
    'THEFT': 'Low',
    'ROBBERY': 'High',
    'SEX OFFENSE': 'High',
    'OTHER OFFENSE': 'Medium',
    'WEAPONS VIOLATION': 'Medium',
    'OFFENSE INVOLVING CHILDREN': 'High',
    'DECEPTIVE PRACTICE': 'Medium',
    'STALKING': 'Medium',
    'MOTOR VEHICLE THEFT': 'Medium',
    'CRIMINAL DAMAGE': 'Medium',
    'CRIMINAL TRESPASS': 'Low',
    'BATTERY': 'Medium',
    'ASSAULT': 'Medium',
    'HOMICIDE': 'High',
    'PROSTITUTION': 'Low',
    'BURGLARY': 'Medium',
    'NARCOTICS': 'Medium',
    'KIDNAPPING': 'High',
    'ARSON': 'High',
    'CONCEALED CARRY LICENSE VIOLATION': 'Medium',
    'CRIMINAL SEXUAL ASSAULT': 'High',
    'INTERFERENCE WITH PUBLIC OFFICER': 'Medium',
    'PUBLIC PEACE VIOLATION': 'Low',
    'LIQUOR LAW VIOLATION': 'Low',
    'INTIMIDATION': 'Medium',
    'GAMBLING': 'Low',
    'OBSCENITY': 'Medium',
    'PUBLIC INDECENCY': 'Low',
    'OTHER NARCOTIC VIOLATION': 'Medium',
    'NON-CRIMINAL': 'Low',
    'HUMAN TRAFFICKING': 'High'
}

def convertCrimeData(crime_data:pd.DataFrame):
    crime_data['Arrest'] = crime_data['Arrest'].replace({
        True:1,
        False:0
    })
    crime_data['New_Date'] = pd.to_datetime(crime_data['Date']) # Create new column
    
    crime_data.dropna(inplace=True) # Drop the NaN values

    crime_data = crime_data[crime_data['Community Area'] != 0] # Dropping the row which contain Community Area as 0
    crime_data['RegionName'] = crime_data['Community Area'].apply(get_community) # change coordinates to neighborhood name
    # crime_data.rename(columns={'Location':'RegionName'}, inplace = True) # Rename the column
    return crime_data


def dropCrimeDataColumns(col:list, crime_data:pd.DataFrame):
    crime_data = crime_data[col]
    return crime_data

def get_community(code):
    return community_areas[code]

def pre_covid_post_covid(crime_data:pd.DataFrame):
    crime_data

    crime_data_2017_2019 = crime_data.copy()
    crime_data_2021_present = crime_data.copy()

    # Pre Covid
    crime_data_2017_2019 = crime_data_2017_2019[(crime_data_2017_2019['New_Date'].dt.year >= 2017) & (crime_data_2017_2019['New_Date'].dt.year <= 2019)]
    
    # print("Before Droping NAN for pre covid")
    # print("Number of NaN value for Location ",crime_data_2017_2019['Location'].isna().sum())
    # print("Number of NaN value for Location Description",crime_data_2017_2019['Location Description'].isna().sum())
    # print("Number of NaN value for Community Area ",crime_data_2017_2019['Community Area'].isna().sum())
    # print("Number of NaN value for Primary Type ",crime_data_2017_2019['Primary Type'].isna().sum(), end="\n\n\n")

    # crime_data_2017_2019.dropna(inplace=True)
    # # checking purpose
    # # print("Min new_date value: ", crime_data_2021_present['New_Date'].min()) # Earliest record of 2021
    # # print(crime_data_2021_present['New_Date'].dt.year.unique()) # Making sure that the range (2021-2024)
    # # checking purpose
    # print("After Droping NAN for pre covid")
    # print("Number of NaN value for Location ",crime_data_2017_2019['Location'].isna().sum())
    # print("Number of NaN value for Location Description",crime_data_2017_2019['Location Description'].isna().sum())
    # print("Number of NaN value for Community Area ",crime_data_2017_2019['Community Area'].isna().sum())
    # print("Number of NaN value for Primary Type ",crime_data_2017_2019['Primary Type'].isna().sum(), end="\n\n\n")


    # Post Covid

    crime_data_2021_present = crime_data_2021_present[crime_data_2021_present['New_Date'].dt.year >= 2021]
    
    crime_data_2021_present['Severity_Score'] = crime_data_2021_present['Primary Type'].map(severity_scores)
    # print("Before Droping NAN for post covid")
    # print("Number of NaN value for Location ",crime_data_2021_present['Location'].isna().sum())
    # print("Number of NaN value for Location Description",crime_data_2021_present['Location Description'].isna().sum())
    # print("Number of NaN value for Community Area ",crime_data_2021_present['Community Area'].isna().sum())
    # print("Number of NaN value for Primary Type ",crime_data_2021_present['Primary Type'].isna().sum(), end="\n\n\n")

    # crime_data_2021_present.dropna(inplace=True)
    # # checking purpose
    # # print("Min new_date value: ", crime_data_2021_present['New_Date'].min()) # Earliest record of 2021
    # # print(crime_data_2021_present['New_Date'].dt.year.unique()) # Making sure that the range (2021-2024)
    # # checking purpose
    # print("After Droping NAN for post covid")
    # print("Number of NaN value for Location ",crime_data_2021_present['Location'].isna().sum())
    # print("Number of NaN value for Location Description",crime_data_2021_present['Location Description'].isna().sum())
    # print("Number of NaN value for Community Area ",crime_data_2021_present['Community Area'].isna().sum())
    # print("Number of NaN value for Primary Type ",crime_data_2021_present['Primary Type'].isna().sum(), end="\n\n\n")

    # crime_data_2017_2019.loc[:, 'Location'] = crime_data_2017_2019['Community Area'].apply(get_community)
    # crime_data_2021_present.loc[:, 'Location'] = crime_data_2021_present['Community Area'].apply(get_community)

    # crime_data_2017_2019.rename(columns={'Location':'RegionName'}, inplace = True)
    # crime_data_2021_present.rename(columns={'Location':'RegionName'}, inplace = True)
    crime_data_2017_2019['Severity_Score'] = crime_data_2017_2019['Primary Type'].map(severity_scores)
    return (crime_data_2017_2019, crime_data_2021_present)


def filterNeighborhood(neighborhood_data:pd.DataFrame):
    neighborhood_data = neighborhood_data[(neighborhood_data['State'] == 'IL') & (neighborhood_data['City'] == 'Chicago')]
    return neighborhood_data

def pre_covid_hd_post_covid_hd(neighborhood_data:pd.DataFrame):
    # Pre Covid
    first_half_column = neighborhood_data.loc[0:, ['RegionName']]
    second_half_column =  neighborhood_data.loc[0:, '2017-01-31':'2019-12-31']

    # Post Covid
    first_half_column_2 = neighborhood_data.loc[0:, ['RegionName']]
    second_half_column_2 =  neighborhood_data.loc[0:, '2021-01-31':]
    neighborhood_data_2017_2019 = pd.concat([first_half_column, second_half_column], axis=1)
    neighborhood_data_2021_present = pd.concat([first_half_column_2, second_half_column_2], axis=1)
    return (neighborhood_data_2017_2019, neighborhood_data_2021_present)

def transpose_data(data:pd.DataFrame):
    data.reset_index(inplace=True)
    neighborhood_names_list = data["RegionName"].to_list()
    data.drop(columns='index', inplace=True)

    map = {}
    for num in range(0,181):
        map[num] = neighborhood_names_list[num]
    data = data.transpose()
    data.rename(columns=map, inplace= True)
    data = data.iloc[1:]
    data.reset_index(inplace=True)
    data.rename(columns={'index':'date'}, inplace=True)

    # droping the column which contain NA value (We can afford to drop a neighborhood)
    data.dropna(axis=1, inplace = True)

    # Converting the price to 2 decimal point
    columns = data.columns.to_list()

    columns = columns[1:]
    for c in columns:
        data[c] = data[c].apply(lambda x: round(x, 2))

    return data.copy()
def main():
    print("Welcome to the Cleaning Process, BE PATIENT WITH ME")
    crime_data = pd.read_csv('csv_files/Crimes_2001_to_Present.csv')
    neighborhood_data = pd.read_csv('csv_files/Neighborhood_House_Price.csv')

    crime_data = convertCrimeData(crime_data) # Convert the crime data to a much suitable format
    
    col = ['ID', 'New_Date', 'Primary Type', 'Location Description', 'Arrest', 'Community Area', 'RegionName']
    crime_data = dropCrimeDataColumns(col, crime_data) # Drop the unnecessary columns
    (pre_covid_data, post_covid_data) = pre_covid_post_covid(crime_data)
    print(pre_covid_data)
    print(post_covid_data)

    neighborhood_data = filterNeighborhood(neighborhood_data)
    (neighborhood_data_2017_2019, neighborhood_data_2021_present) = pre_covid_hd_post_covid_hd(neighborhood_data)
    neighborhood_data_2017_2019 = transpose_data(neighborhood_data_2017_2019)
    neighborhood_data_2021_present = transpose_data(neighborhood_data_2021_present)

    print(neighborhood_data_2017_2019)
    print(neighborhood_data_2021_present)

    pre_covid_data.to_csv('csv_files/Crimes_2021_to_Present.csv', index=False)
    pre_covid_data.to_csv('csv_files/Crimes_2017_to_2019.csv', index=False)

    neighborhood_data_2017_2019.to_csv('csv_files/neighborhood_data_2017_2019.csv', index = False)
    neighborhood_data_2021_present.to_csv('csv_files/neighborhood_data_2021_present.csv', index = False)

    
if __name__ == "__main__":
    main()
