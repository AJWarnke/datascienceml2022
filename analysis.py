import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def get_basic_overview(data):
    print(data.head())
    print(data.describe(), '\n')
    print(data.isna().any(), '\n')


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


def split_data(data):
    data_wo_leap = data
    data_wo_leap = data_wo_leap.drop([1154])
    data_wo_leap = data_wo_leap.drop([1154 + 1460 + 2])


if __name__ == '__main__':
    data = pd.read_csv('data/Kaub_Level_Since_2013.csv')
    get_basic_overview(data)
    linear_regression(data)
    split_data(data)
    # plt.show()
