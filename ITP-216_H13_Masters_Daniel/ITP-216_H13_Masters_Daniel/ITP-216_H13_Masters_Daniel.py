# Name: Daniel Masters
# Spring 2022
# Section: 31883
# ITP 216 Homework 13

import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("2953515.csv")     #read in the csv as a dataframe
    df = df.dropna(axis=0, subset='TOBS')   #removing all rows with NaN in temp column
    df['YEAR'] = df['DATE'].str[:4]         #created year column using the first 4 numbers in the date
    df['MONTH_DAY'] = df['DATE'].str[5:]    #month and day recorded with remaining numbers
    year_one = df[df['YEAR'] == '2017']     #created dataframes based on each year
    year_two = df[df['YEAR'] == '2018']
    year_three = df[df['YEAR'] == '2019']
    year_four = df[df['YEAR'] == '2020']
    year_five = df[df['YEAR'] == '2021']
    year_six = df[df['YEAR'] == '2022']
    fig, ax = plt.subplots(2, 1, figsize=(10,10))   #creating two subplots
    #group each year by the mean of each day and index by each month/day for x-axis and index by TOBS or temps for each day
    #labelled and created legend for the different lines
    ax[0].plot(year_one.groupby('MONTH_DAY', as_index=False).mean()['MONTH_DAY'], year_one.groupby('MONTH_DAY', as_index=False).mean()['TOBS'], label= '2017')
    ax[0].plot(year_two.groupby('MONTH_DAY', as_index=False).mean()['MONTH_DAY'], year_two.groupby('MONTH_DAY', as_index=False).mean()['TOBS'], label='2018')
    ax[0].plot(year_three.groupby('MONTH_DAY', as_index=False).mean()['MONTH_DAY'], year_three.groupby('MONTH_DAY', as_index=False).mean()['TOBS'], label='2019')
    ax[0].plot(year_four.groupby('MONTH_DAY', as_index=False).mean()['MONTH_DAY'], year_four.groupby('MONTH_DAY', as_index=False).mean()['TOBS'], label='2020')
    ax[0].plot(year_five.groupby('MONTH_DAY', as_index=False).mean()['MONTH_DAY'], year_five.groupby('MONTH_DAY', as_index=False).mean()['TOBS'], label='2021')
    ax[0].plot(year_six.groupby('MONTH_DAY', as_index=False).mean()['MONTH_DAY'], year_six.groupby('MONTH_DAY', as_index=False).mean()['TOBS'], label='2022')
    ax[0].set_xticks([0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334])      #set monthly numbs w/ xticks
    ax[0].set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']) #changing the labels
    ax[0].set_xlabel('Month')
    ax[0].set_ylabel('Temp (F)')
    ax[0].set_title("Yearly climatological data for zip 90089 from 2017 to 2022")
    ax[0].legend()
    #creating subplot #2
    #same logic as first subplot
    #the x is grouped by the month_day and indexed by month day, the height is the same only indexed by the temps
    #each index is converted to a list and graphed
    #labelled and created legend for historical and current averages
    ax[1].bar(x=df.groupby("MONTH_DAY", as_index=False).mean()["MONTH_DAY"].tolist(), height=df.groupby("MONTH_DAY", as_index=False).mean()["TOBS"].tolist(), label='historical average')
    df_grouped_two = year_five.groupby("MONTH_DAY", as_index=False).mean()
    ax[1].bar(x=df_grouped_two["MONTH_DAY"].tolist(), height=df_grouped_two["TOBS"].tolist(), label='2021')
    ax[1].set_xticks([0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334])
    ax[1].set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Temp (F)')
    ax[1].set_title("Comparing current year and historical averages")
    ax[1].legend()
    plt.show()

if __name__ == '__main__':
    main()




