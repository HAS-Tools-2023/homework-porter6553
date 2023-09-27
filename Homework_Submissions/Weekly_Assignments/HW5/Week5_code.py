# Homework 5

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week5.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)

# %%
# DON'T change this part -- this creates the lists you 
# should use for the rest of the assignment
# no need to worry about how this is being done now we will cover
# this in later sections. 

#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=31,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

#Drop NaN Values from Dataset
data = data.dropna()

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# Make a numpy array of this data
flow_data = data[['year', 'month','day', 'flow']].to_numpy()

# Array of data between 2015 and 2019
flow_5yr = flow_data[(flow_data[:,0] >= 2015) & (flow_data[:,0] <= 2019),:]
print(flow_5yr)
# Dimensions of flow_5yr
print(np.shape(flow_5yr))
# Average for the flow over the 5 year period
print(np.mean(flow_5yr[:, 3]))

#%%
# For loop for average flow over the 5 year period
a=[]
for i in range(len(flow_5yr)):
    a = np.append(a, flow_5yr[i,3])
print(np.mean(a))

# %%
# Convert the daily average flow from cubic feet per second to cubic feet
## cubic feet per second x 60 sec/min x 60 min/hour x 24 hours/day = 86400 cubic feet/day
print(flow_5yr[:,3] * 86400)
flow_daily=[]
for i in range(len(a)):
    cf = (flow_5yr[i, 3]) * 86400
    flow_daily = np.append(flow_daily, cf)
    print(flow_daily)
print(flow_daily)
print(flow_daily.size)
print(np.sum(flow_daily))

# %%
# Timeseries of monthly average flow with 60 rows and 3 columns
flow_monthly = np.zeros((60, 3))
flow_monthly[:,0] = np.tile(np.arange(2015, 2020, 1), 12) #Must go to 2020 because it isn't inclusive
flow_monthly[:,1] = np.tile(np.arange(1, 13, 1), 5)
#print(flow_monthly[:, 0])
for i in range(60):
    year_temp = flow_monthly[i, 0]
    month_temp = flow_monthly[i, 1]
    #print(year_temp)
    #print(month_temp)
    ilist = (flow_5yr[:,0] == year_temp) & (flow_5yr[:,1] == month_temp)
    c = np.mean(flow_5yr[ilist,3])
    print(c)

# %%
