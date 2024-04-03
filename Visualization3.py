import pandas as pd
import plotly.express as px

# Load the cleaned and processed crime data from 2017 to 2019
crime_data = pd.read_csv('csv_files/Crimes_2017_to_2019.csv')

# Group by 'RegionName' to get crime counts
crime_count = crime_data.groupby('RegionName').size().reset_index(name='CrimeCount')

# Load the transposed neighborhood housing price data from 2017 to 2019
housing_data = pd.read_csv('csv_files/neighborhood_data_2017_2019.csv')

# Melt the housing data to long format and calculate the average housing prices per neighborhood
housing_data_long = housing_data.melt(id_vars=['date'], var_name='Neighborhood', value_name='HousingPrice')
housing_data_long['date'] = pd.to_datetime(housing_data_long['date'])
avg_housing_prices = housing_data_long.groupby('Neighborhood')['HousingPrice'].mean().reset_index()

# Merge the datasets on the neighborhood names
merged_data = crime_count.merge(avg_housing_prices, left_on='RegionName', right_on='Neighborhood')

# Determine the quartiles for crime count
merged_data['CrimeQuartile'] = pd.qcut(merged_data['CrimeCount'], 4, labels=['Q1', 'Q2', 'Q3', 'Q4'])

# Create the interactive boxplot for housing prices by crime rate quartile using Plotly
fig = px.box(merged_data, x='CrimeQuartile', y='HousingPrice',
             labels={'CrimeQuartile': 'Crime Rate Quartile', 'HousingPrice': 'Average Housing Price'},
             title='Interactive Boxplot of Housing Prices by Crime Rate Quartile')

# Show the figure
fig.show()






