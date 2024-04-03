import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

selected_neighborhoods = [
        "Near West Side",
        "West Town",
        "Loop",
        "Near North Side",
        "Near South Side",
        "Lower West Side",
        "East Garfield Park",
        "North Lawndale",
        "South Lawndale",
        "Humboldt Park",
    ]

def visualization_one():

    precovid_df = pd.read_csv('csv_files/Crimes_2017_to_2019.csv')
    postcovid_df = pd.read_csv('csv_files/Crimes_2021_to_Present.csv')

    precovid_df['Period'] = 'Pre-Covid'
    postcovid_df['Period'] = 'Post-Covid'
    combined_df = pd.concat([precovid_df, postcovid_df])
    # columns_names = combined_df.columns
    # print(columns_names)

    data_plot = combined_df[combined_df['RegionName'].isin(selected_neighborhoods)]

    plt.figure(figsize=(12, 6))
    sns.histplot(data=data_plot, x='RegionName', hue='Period', multiple='dodge', shrink= 0.8, palette='mako')
    plt.xticks(rotation=45)
    plt.xlabel('Neighborhood')
    plt.ylabel('Frequency of Crime')
    plt.title('Frequency of Crime Pre and Post Covid by Neighborhood')
    plt.tight_layout()
    plt.show()

def main():
    visualization_one()






