import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



selected_neighborhoods2 = [
        "Near West Side",
        "West Town",
        "Loop",
        "Near North Side",
        "Near South Side",
        "Lower West Side",
        "Armor Square",
        "East Garfield Park",
        "North Lawndale",
        "South Lawndale",
        "Humboldt Park",
        "Bridgeport",
        "McKinley Park",
        "West Garfield Park",
        "Logan Square",
        "Lincoln Park",
        "Hermosa",
    ]

pop_data2 = {
        "Near West Side": 67881,
        "West Town": 87781,
        "Loop": 42298,
        "Near North Side": 105481,
        "Near South Side": 28795,
        "Lower West Side": 33751,
        "Armor Square": 13890,
        "East Garfield Park": 19992, 
        "North Lawndale": 34794,
        "South Lawndale": 71399,
        "Humboldt Park": 54165,
        "Bridgeport": 33702,
        "McKinley Park": 15923,
        "West Garfield Park": 17433,
        "Logan Square": 71665,
        "Lincoln Park": 40494,
        "Hermosa": 24062
}


def visualization2():
    postcovid_df = pd.read_csv('csv_files/Crimes_2021_to_Present.csv')
    
    filteredpostcovid_df = postcovid_df[postcovid_df['RegionName'].isin(selected_neighborhoods2)]

    crime_counts = filteredpostcovid_df.groupby(['RegionName', 'Primary Type']).size().reset_index(name='Count')

    crime_by_location = filteredpostcovid_df.groupby('RegionName').size().reset_index(name='TotalCount')

    crime_by_location['Population'] = crime_by_location['RegionName'].map(pop_data2)

    crime_by_location['Crimes per 1000'] = (crime_by_location['TotalCount']/ crime_by_location['Population']) *1000

    crime_with_totals = crime_counts.merge(crime_by_location[['RegionName', 'Population', 'Crimes per 1000']], on='RegionName')

    crime_with_totals['Rate per 1000'] = (crime_with_totals['Count'] / crime_with_totals['Population']) *1000

    pivot_table = crime_with_totals.pivot(index='RegionName', columns= 'Primary Type', values = 'Rate per 1000')

    total_pop = sum(pop_data2.values())

    overall = crime_with_totals.groupby('Primary Type')['Count'].sum() / total_pop *1000
    overall = overall.reset_index(name='Overall')

    sorted = overall.sort_values(by='Overall', ascending=False)['Primary Type']

    pivot_table = pivot_table[sorted]

    plt.figure(figsize=(10,6))
    sns.heatmap(pivot_table, annot=False, cmap='coolwarm', linecolor='white', linewidths=0.05)
    plt.title('Crime Rate per 1000 People by Crime Types and Location')
    #plt.title('Theft and Battery are the most frequently committed crimes\nespecially in the neighborhoods of Lincoln Park and the Loop')
    plt.ylabel('Neighborhoods')
    plt.xlabel('Type of Crime')
    plt.xticks(rotation=85, fontsize = 8)
    plt.yticks(fontsize=10)
    plt.tight_layout()
    plt.show()

# def main():
#     visualization2()

# if __name__ == "__main__":
#     main()



