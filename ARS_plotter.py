import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from ARS_reader import ARS_reader

"""
This code will create basic plots of ARS data from 2020
hopefully it can be automated for the current (2025) data?
"""

f_ben = '/Users/jacksontobin/Local_Documents/NightTime_Research/SQM/ARS_2020/BEN 2020 PM25.csv'
f_sop = '/Users/jacksontobin/Local_Documents/NightTime_Research/SQM/ARS_2020/SOP 2020 PM25.csv'
f_fos = '/Users/jacksontobin/Local_Documents/NightTime_Research/SQM/ARS_2020/FOS 2020 PM25.csv'
f_dis = '/Users/jacksontobin/Local_Documents/NightTime_Research/SQM/ARS_2020/DIS 2020 PM25.csv'

ben_obj = ARS_reader(f_ben)
ben_df = ben_obj.dataframe
fos_df = ARS_reader(f_fos).dataframe
sop_df = ARS_reader(f_sop).dataframe
dis_df = ARS_reader(f_dis).dataframe

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(15, 8))
ax.scatter(ben_df["Date"], ben_df["AQI"], marker=',', s=2, c='b')
ax.scatter(fos_df['Date'], fos_df["AQI"], marker=',', s=2, c='r')
ax.scatter(sop_df['Date'], sop_df["AQI"], marker=',', s=2, c='g')
ax.scatter(dis_df['Date'], dis_df["AQI"], marker=',', s=2)
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