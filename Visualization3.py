import pandas as pd
import plotly.express as px


crime_data = pd.read_csv('csv_files/Crimes_2017_to_2019.csv')

crime_count = crime_data.groupby('RegionName').size().reset_index(name='CrimeCount')


housing_data = pd.read_csv('csv_files/neighborhood_data_2017_2019.csv')

housing_data_long = housing_data.melt(id_vars=['date'], var_name='Neighborhood', value_name='HousingPrice')
housing_data_long['date'] = pd.to_datetime(housing_data_long['date'])

avg_housing_prices = housing_data_long.groupby('Neighborhood')['HousingPrice'].mean().reset_index()

# merging datasets
merged_data = crime_count.merge(avg_housing_prices, left_on='RegionName', right_on='Neighborhood')

#quartiles for crime count
merged_data['CrimeQuartile'] = pd.qcut(merged_data['CrimeCount'], 4, labels=['Q1', 'Q2', 'Q3', 'Q4'])


fig = px.box(merged_data, x='CrimeQuartile', y='HousingPrice',
             labels={'CrimeQuartile': 'Crime Rate Quartile', 'HousingPrice': 'Average Housing Price'},
             title='Interactive Boxplot of Housing Prices by Crime Rate Quartile')
fig.show()






