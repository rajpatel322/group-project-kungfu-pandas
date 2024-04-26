import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define neighborhoods and population data
selected_neighborhoods = [
    "Near West Side", "West Town", "Loop", "Near North Side",
    "Near South Side", "Lower West Side", "East Garfield Park",
    "North Lawndale", "South Lawndale", "Humboldt Park",
]

pop_data = {
    "Near West Side": 67881, "West Town": 87781, "Loop": 42298,
    "Near North Side": 105481, "Near South Side": 28795,
    "Lower West Side": 33751, "East Garfield Park": 19992,
    "North Lawndale": 34794, "South Lawndale": 71399, "Humboldt Park": 54165
}

def load_and_prepare_data(file_path, crime_type):
    df = pd.read_csv(file_path)
    df = df[df['Primary Type'] == crime_type]
    return df

def visualization_one():
    precovid_df = load_and_prepare_data('csv_files/Crimes_2017_to_2019.csv', 'THEFT')
    postcovid_df = load_and_prepare_data('csv_files/Crimes_2021_to_Present.csv', 'THEFT')

    
    precovid_df['Period'] = 'Pre-Covid'
    postcovid_df['Period'] = 'Post-Covid'

    
    combined_df = pd.concat([precovid_df, postcovid_df])
    data_plot = combined_df[combined_df['RegionName'].isin(selected_neighborhoods)]

    
    data_plot['Population'] = data_plot['RegionName'].map(pop_data)
    data_plot['Crime Rate per 1000'] = data_plot.groupby(['RegionName', 'Period'])['ID'].transform('count') / data_plot['Population'] * 1000

    # Visualize data
    plt.figure(figsize=(12, 6))
    sns.histplot(data=data_plot, x='RegionName', hue='Period', multiple='dodge', shrink=0.8, palette='mako')
    plt.xticks(rotation=45)
    plt.xlabel('Neighborhood')
    plt.ylabel('Frequency of Theft per 1000 People')
    plt.title('Frequency of Theft Pre and Post Covid by Neighborhood')
    plt.tight_layout()
    plt.show()

def main():
    visualization_one()

if __name__ == "__main__":
    main()
