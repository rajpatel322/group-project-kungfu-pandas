import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualization_theft():
    crime_data = pd.read_csv('csv_files/Crimes_2021_to_Present.csv')
    theft_data = crime_data[crime_data['Primary Type'] == 'THEFT']
    
    theft_count = theft_data.groupby('RegionName').size().reset_index(name='CrimeCount')
    
    housing_data = pd.read_csv('csv_files/neighborhood_data_2017_2019.csv')
    housing_data_long = housing_data.melt(id_vars=['date'], var_name='Neighborhood', value_name='HousingPrice')
    housing_data_long['date'] = pd.to_datetime(housing_data_long['date'])
    
    avg_housing_prices = housing_data_long.groupby('Neighborhood')['HousingPrice'].mean().reset_index()
    
    merged_data_theft = theft_count.merge(avg_housing_prices, left_on='RegionName', right_on='Neighborhood')
    
    merged_data_theft['CrimeQuartile'] = pd.qcut(merged_data_theft['CrimeCount'], 4, labels=['Q1', 'Q2', 'Q3', 'Q4'])

    plt.figure(figsize=(12, 8))
    sns.set(style="whitegrid")
    
    boxplot = sns.boxplot(x='CrimeQuartile', y='HousingPrice', data=merged_data_theft, palette="Set2", showfliers=False)
    
    boxplot.set_title('Boxplot of Housing Prices by Theft Crime Rate Quartile', fontsize=16)
    boxplot.set_xlabel('Theft Crime Rate Quartile', fontsize=14)
    boxplot.set_ylabel('Average Housing Price ($)', fontsize=14)
    boxplot.tick_params(labelsize=12)
    
    plt.grid(axis='y', linestyle='--', linewidth=0.7)
    plt.tight_layout()
    plt.show()

visualization_theft()
