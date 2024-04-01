import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

precovid_df = pd.read_csv('csv_files/Crimes_2017_to_2019.csv')
postcovid_df = pd.read_csv('csv_files/Crimes_2021_to_Present.csv')
prehousing_df = pd.read_csv('csv_files/neighbor')