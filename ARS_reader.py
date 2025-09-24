import pandas as pd
import numpy as np
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

class ARS_reader(object):    
    def __init__(self, path):
        df = pd.read_csv(path)
        
        # Add titles to the columns
        df.columns = ["Location", "Date", "Particulate", "AQI"]
        # Reset the date/times to a DateTime object
        df["Date"] = df["Date"].apply(date_rename)
        # Remove AQI less than 0 (not possible)
        df['AQI'] = df['AQI'].apply(lambda x: np.nan if (x < 0) else x)

        # Instantiate object variables
        # Allow access to DataFrame: This allows for easier processing downstream
        self.dataframe = df
        # Allow access to ndarrays for easier, short-term access
        self.date = df["Date"]
        self.location = df["Location"]
        self.aqi = df["AQI"]
        self.particulate = df["Particulate"]