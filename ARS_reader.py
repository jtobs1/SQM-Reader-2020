import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

"""
This code aims to read data (csv) from Scott Cismoski, of the ARS PurpleAir hourly
PM2.5 measurements.

File naming:
    SOP: Soapstone Prairie
    BEN: Bench at Gardens on Spring Creek
    DIS: Discovery Museum
    FOS: Fossil Creek
"""

f_ben = '/Users/jacksontobin/Local_Documents/NightTime_Research/SQM/ARS_2020/BEN 2020 PM25.csv'
f_sop = '/Users/jacksontobin/Local_Documents/NightTime_Research/SQM/ARS_2020/SOP 2020 PM25.csv'
f_fos = '/Users/jacksontobin/Local_Documents/NightTime_Research/SQM/ARS_2020/FOS 2020 PM25.csv'
f_dis = '/Users/jacksontobin/Local_Documents/NightTime_Research/SQM/ARS_2020/DIS 2020 PM25.csv'

data_ben = pd.read_csv(f_ben)

print(type(data_ben))