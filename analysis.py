import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def get_basic_overview(data):
    print(data.head())
    print(data.describe(), '\n')
    print(data.isna().any(), '\n')
    quantile1, quantile3 = data['level'].quantile([0.25, 0.75])
    IQR = quantile3 - quantile1
    lower = quantile1 - (1.5 * IQR)
    upper = quantile3 + (1.5 * IQR)
    outlier = []
    for level in data['level']:
        if level < lower or level > upper:
            outlier.append(level)

    print(r'We have {} outlier in our data from a total of {} data points. \nThat makes it a percentage of {}\% number_of_outliers/total_data'.format(
        len(outlier), len(data['level']), len(outlier) / len(data['level'])))


def linear_regression(data):
    plt.figure(1)
    CB91_Blue = '#2CBDFE'
    CB91_Green = '#47DBCD'
    color_list = [CB91_Blue, CB91_Green]
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=color_list)
    plt.plot(np.arange(len(data.index)), data['level'])
    m, b = np.polyfit(np.arange(len(data.index)), data['level'], 1)
    plt.plot(np.arange(len(data.index)), m * np.arange(len(data.index)) + b)
    plt.xlabel('Day')
    plt.ylabel('Water Level')
    plt.title('The water levels of the rhine')
    plt.legend(['Water Levels', 'Linear Regression'], frameon=False)


def split_data_monthly(data):
    data['month'] = pd.DatetimeIndex(data['date']).month_name()
    monthly_median = data.groupby('month').agg(
        {'level': np.median}).reset_index()
    monthly_mean = data.groupby('month').agg({'level': np.mean}).reset_index()
    return monthly_mean, monthly_median


def box_plot(data):
    plt.figure(2)
    sns.set_theme(style="whitegrid")
    ax = sns.boxplot(x=data['level'])


def bar_plot(monthly_mean, monthly_median):
    plt.figure(3)
    sns.barplot(x="month", y="level", data=monthly_median)
    plt.figure(4)
    sns.barplot(x="month", y="level", data=monthly_mean)


if __name__ == '__main__':
    data = pd.read_csv('data/Kaub_Level_Since_2013.csv')
    get_basic_overview(data)
    monthly_mean, monthly_median = split_data_monthly(data)

    linear_regression(data)

    box_plot(data)
    bar_plot(monthly_mean, monthly_median)
    # plt.show()
