import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

postcovid_df = pd.read_csv('csv_files/Crimes_2021_to_Present.csv')

selected_neighborhoods2 = [
        "Armor Square",
        "Bridgeport",
        "East Garfield Park",
        "Hermosa",
        "Humboldt Park",
        "Lincoln Park",
        "Logan Square",
        "Loop",
        "Lower West Side",
        "McKinley Park",
        "Near North Side",
        "Near South Side",
        "Near West Side",
        "North Lawndale",
        "South Lawndale",
        "West Garfield Park",
        "West Town",
    ]

filteredpostcovid_df = postcovid_df[postcovid_df['RegionName'].isin(selected_neighborhoods2)]

crime_counts = filteredpostcovid_df.groupby(['RegionName', 'Primary Type']).size().reset_index(name='Count')

crime_by_location = filteredpostcovid_df.groupby('RegionName').size().reset_index(name='TotalCount')

crime_with_totals = crime_counts.merge(crime_by_location, on='RegionName')

crime_with_totals['Percentage'] = (crime_with_totals['Count'] / crime_with_totals['TotalCount']) *100

pivot_table = crime_with_totals.pivot(index='RegionName', columns= 'Primary Type', values = 'Percentage')

plt.figure(figsize=(14,10))
sns.heatmap(pivot_table, annot=False, cmap='viridis', linecolor='white', linewidths=0.1)
plt.title('Percentage Distribution of Crime Types by Location')
plt.ylabel('Neighborhoods')
plt.xlabel('Primary Type')
plt.xticks(rotation=85, fontsize = 8)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()