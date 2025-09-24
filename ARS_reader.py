import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import sys
import datetime

"""
This code aims to read data (csv) from Scott Cismoski, of the ARS PurpleAir hourly
PM2.5 measurements.

File naming:
    SOP: Soapstone Prairie
    BEN: Bench at Gardens on Spring Creek
    DIS: Discovery Museum
    FOS: Fossil Creek
Dataframe structure:
    column 1: location (3-digit number)
    column 2: date (mm/dd/yyyy) and time (24hr local)
    column 3: particulate type (PM2.5PA-1)
    column 4: PM2.5 measurment (AQI)
"""

def date_rename(date):
    '''Turns date strings into datetime objects.'''
    return datetime.datetime.strptime(date, r'%m/%d/%Y %H:%M')

f_ben = '/Users/jacksontobin/Local_Documents/NightTime_Research/SQM/ARS_2020/BEN 2020 PM25.csv'
f_sop = '/Users/jacksontobin/Local_Documents/NightTime_Research/SQM/ARS_2020/SOP 2020 PM25.csv'
f_fos = '/Users/jacksontobin/Local_Documents/NightTime_Research/SQM/ARS_2020/FOS 2020 PM25.csv'
f_dis = '/Users/jacksontobin/Local_Documents/NightTime_Research/SQM/ARS_2020/DIS 2020 PM25.csv'

data_ben = pd.read_csv(f_ben)

# Rename the Columns
data_ben.rename(columns={'45.96':'AQI', '731':'Location', '1/1/2020 0:00':'Date'}, inplace=True)
data_ben['Date'] = data_ben['Date'].apply(date_rename)
data_ben['AQI'] = data_ben['AQI'].apply(lambda x: np.nan if (x < 0) else x)

# Plot the data
fig, ax = plt.subplots()
plt.scatter(data_ben['Date'], data_ben['AQI'], s=1)
plt.xlabel('Date')
plt.ylabel('AQI')
plt.show()
plt.close()