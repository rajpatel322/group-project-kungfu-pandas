import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

def ttest_uic_theft(data:pd.DataFrame, data2:pd.DataFrame):
    '''This test is used when you have one group of participants measured at two 
    different time points or under two different conditions. For example, you might 
    use a paired samples t-test to compare the blood pressure of individuals before 
    and after a treatment. '''
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
    data = data[data['RegionName'].isin(selected_neighborhoods)]
    data = data[data['Primary Type'] == 'THEFT']
    #print(data)
    data2 = data2[data2['RegionName'].isin(selected_neighborhoods)]
    data2 = data2[data2['Primary Type'] == 'THEFT']


    preCovid = (data.groupby(['RegionName']).count().reset_index())
    postCovid = (data2.groupby(['RegionName']).count().reset_index())

    preCovid.rename(columns={'Arrest':'NUM CRIME'}, inplace=True)
    postCovid.rename(columns={'Arrest':'NUM CRIME'}, inplace=True)

    preCovid = preCovid[['RegionName', 'NUM CRIME']]
    postCovid = postCovid[['RegionName', 'NUM CRIME']]

    # print(preCovid)
    # print(postCovid)

    t_stat, pval = stats.ttest_rel(np.log(preCovid['NUM CRIME']).to_list(), np.log(postCovid['NUM CRIME']).to_list())
    print(t_stat, pval)

    if pval < 0.05:
        if t_stat > 0:
            print("Reject the NULL Hypothesis: There is a significant decrease in theft post COVID compared to pre COVID")
        else:
            print("Reject the NULL Hypothesis: There is a significant increase in theft post COVID compared to pre COVID")    
    else:
        print("Fail to reject the NULL hypothesis: There is no significant difference in theft between pre and post covid")

    # plt.figure(figsize=(12, 6))

    # plt.subplot(1, 2, 1)
    # plt.hist(np.log(preCovid['NUM CRIME']), bins=30, color='blue', alpha=0.7)
    # plt.title('Pre-COVID Crime Data')
    # plt.xlabel('Number of Crimes')
    # plt.ylabel('Frequency')

    # plt.subplot(1, 2, 2)
    # plt.hist(np.log(postCovid['NUM CRIME']), bins=30, color='red', alpha=0.7)
    # plt.title('Post-COVID Crime Data')
    # plt.xlabel('Number of Crimes')
    # plt.ylabel('Frequency')

    # plt.tight_layout()
    # plt.show()


def ttest_uic_battery(data:pd.DataFrame, data2:pd.DataFrame):
    '''This test is used when you have one group of participants measured at two 
    different time points or under two different conditions. For example, you might 
    use a paired samples t-test to compare the blood pressure of individuals before 
    and after a treatment. '''
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
    data = data[data['RegionName'].isin(selected_neighborhoods)]
    data = data[data['Primary Type'] == 'BATTERY']
    #print(data)
    data2 = data2[data2['RegionName'].isin(selected_neighborhoods)]
    data2 = data2[data2['Primary Type'] == 'BATTERY']



    preCovid = (data.groupby(['RegionName']).count().reset_index())
    postCovid = (data2.groupby(['RegionName']).count().reset_index())

    preCovid.rename(columns={'Arrest':'NUM CRIME'}, inplace=True)
    postCovid.rename(columns={'Arrest':'NUM CRIME'}, inplace=True)

    preCovid = preCovid[['RegionName', 'NUM CRIME']]
    postCovid = postCovid[['RegionName', 'NUM CRIME']]

    # print(preCovid)
    # print(postCovid)

    t_stat, pval = stats.ttest_rel(np.log(preCovid['NUM CRIME']).to_list(), np.log(postCovid['NUM CRIME']).to_list())
    print(t_stat, pval)

    if pval < 0.05:
        if t_stat > 0:
            print("Reject the NULL Hypothesis: There is a significant decrease in battery post COVID compared to pre COVID")
        else:
            print("Reject the NULL Hypothesis: There is a significant increase in battery post COVID compared to pre COVID")  
    else:
        print("Fail to reject the NULL hypothesis: There is no significant difference in battery between pre and post covid")

    # plt.figure(figsize=(12, 6))

    # plt.subplot(1, 2, 1)
    # plt.hist(np.log(preCovid['NUM CRIME']), bins=30, color='blue', alpha=0.7)
    # plt.title('Pre-COVID Crime Data')
    # plt.xlabel('Number of Crimes')
    # plt.ylabel('Frequency')

    # plt.subplot(1, 2, 2)
    # plt.hist(np.log(postCovid['NUM CRIME']), bins=30, color='red', alpha=0.7)
    # plt.title('Post-COVID Crime Data')
    # plt.xlabel('Number of Crimes')
    # plt.ylabel('Frequency')

    # plt.tight_layout()
    # plt.show()


def main():
    pre = pd.read_csv('csv_files/Crimes_2017_to_2019.csv')
    post = pd.read_csv('csv_files/Crimes_2021_to_Present.csv')

    ttest_uic_battery(pre, post)

def main2():
    pre = pd.read_csv('csv_files/Crimes_2017_to_2019.csv')
    post = pd.read_csv('csv_files/Crimes_2021_to_Present.csv')

    ttest_uic_theft(pre, post)

    

# if __name__ == "__main__":
#     main()

# if __name__ == "__main__":
#     main2()