import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualization1():
    crime_data = pd.read_csv('csv_files/Crimes_2021_to_Present.csv')
    crime_data = crime_data[crime_data['Primary Type'].isin(['THEFT', 'BATTERY'])]
    
    crime_count = crime_data.groupby('RegionName').size().reset_index(name='CrimeCount')
    
    housing_data = pd.read_csv('csv_files/neighborhood_data_2017_2019.csv')
    housing_data_long = housing_data.melt(id_vars=['date'], var_name='Neighborhood', value_name='HousingPrice')
    housing_data_long['date'] = pd.to_datetime(housing_data_long['date'])
    
    avg_housing_prices = housing_data_long.groupby('Neighborhood')['HousingPrice'].mean().reset_index()
    
    merged_data = crime_count.merge(avg_housing_prices, left_on='RegionName', right_on='Neighborhood')
    
    merged_data['CrimeQuartile'] = pd.qcut(merged_data['CrimeCount'], 4, labels=['Q1', 'Q2', 'Q3', 'Q4'])

    # Printing the merged data and statistics
    print(merged_data)
    print("25th percentile crime's avg housing price: ", merged_data[merged_data['CrimeQuartile'] == 'Q1']['HousingPrice'].median())
    print("50th percentile crime's avg housing price: ", merged_data[merged_data['CrimeQuartile'] == 'Q2']['HousingPrice'].median())
    print("75th percentile crime's avg housing price: ", merged_data[merged_data['CrimeQuartile'] == 'Q3']['HousingPrice'].median())
    print("100th percentile crime's avg housing price: ", merged_data[merged_data['CrimeQuartile'] == 'Q4']['HousingPrice'].median())

    # Visualization
    plt.figure(figsize=(12, 8))
    sns.set(style="whitegrid")
    
    boxplot = sns.boxplot(x='CrimeQuartile', y='HousingPrice', data=merged_data, palette="Set2", showfliers=False)
    sns.stripplot(x='CrimeQuartile', y='HousingPrice', data=merged_data, color=".25", jitter=True, size=4)
    
    boxplot.set_title('Boxplot of Housing Prices by Crime Rate Quartile', fontsize=16)
    boxplot.set_xlabel('Crime Rate Quartile', fontsize=14)
    boxplot.set_ylabel('Average Housing Price ($)', fontsize=14)
    boxplot.tick_params(labelsize=12)

    for quartile in merged_data['CrimeQuartile'].unique():
       median = merged_data[merged_data['CrimeQuartile'] == quartile]['HousingPrice'].median()
       plt.text(x=quartile, y=median, s=f"Median: {median:.2f}", horizontalalignment='center')
    
    plt.grid(axis='y', linestyle='--', linewidth=0.7)
    plt.tight_layout()
    plt.show()


visualization1()
