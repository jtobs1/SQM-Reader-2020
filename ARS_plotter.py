import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from ARS_reader import ARS_reader
import sys

"""
This code will create basic plots of ARS data from 2020
hopefully it can be automated for the current (2025) data?
"""

def monthly_average(dataframe):
    # Creates a dataframe with one row/month and the monthly averages of AQI.
    dataframe["Monthly Average"] = dataframe.groupby(dataframe["Date"].dt.to_period("M"))["AQI"].transform("mean")
    dataframe["Monthly Standard Deviation"] = dataframe.groupby(dataframe["Date"].dt.to_period("M"))["AQI"].transform('std')
    # return dataframe

f_ben = '/Users/jacksontobin/Local_Documents/NightTime_Research/SQM/ARS_2020/BEN 2020 PM25.csv'
f_sop = '/Users/jacksontobin/Local_Documents/NightTime_Research/SQM/ARS_2020/SOP 2020 PM25.csv'
f_fos = '/Users/jacksontobin/Local_Documents/NightTime_Research/SQM/ARS_2020/FOS 2020 PM25.csv'
f_dis = '/Users/jacksontobin/Local_Documents/NightTime_Research/SQM/ARS_2020/DIS 2020 PM25.csv'

ben_obj = ARS_reader(f_ben)
ben_df = ben_obj.dataframe
monthly_average(ben_df)
print(ben_df["Monthly Average"])
print(ben_df["Monthly Standard Deviation"])

plt.scatter(ben_df['Date'], ben_df["Monthly Average"])
plt.show()
plt.close()

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(15, 8))
ax.scatter(ben_df["Date"], (ben_df["AQI"]), marker=',', s=2, c='b')
ax.set_xlabel("Date")
ax.set_ylabel("AQI PM2.5")
ax.set_title("Hourly PM2.5 AQI: Bench at Spring Creek Trail")
plt.show()
plt.close()

# I eventually want to make this a modular class, so I can add any number of locations and datasets easily.
# class PlotGenerator:
#     def __init__(self, dataframe):
#         self.dataframe = dataframe
#     def plot_scatter(self, dataframe, n_rows, n_cols, figsize):
#         fig, ax = plt.subplots(nrows=n_rows, ncols=n_cols, figsize=figsize)
# if __name__ == "__main__":