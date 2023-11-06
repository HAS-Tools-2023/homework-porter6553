## Exercises for thursday's class
#%%
import os
import pandas as pd
import matplotlib.pyplot as plt
#%%
# Exercise 1
# modify the following to create a pandas dataframe where the column 'datetime' is a datetime object. You should do this two ways: (1) by modifying the read.table function arguments directly. (2) keeping the read.table line I have below the same and modifying the dataframe after the fact. 
# How can you check to confirm that what you did worked? 
data = pd.read_table('streamflow_demo.txt', sep='\t',skiprows=30, names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'], index_col=['datetime'], parse_dates=['datetime'])


data.info()

# Method 2

# Exercise 2: 
data = pd.read_table('streamflow_demo.txt', sep='\t',skiprows=30, names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'], parse_dates=['datetime'])

data1 = data.set_index('datetime')
data1.info
#%%
#2.1: Read the 'daymet.csv' file in as a data frame using the 'date' column as the index and making sure to treat that column as a datetime object. 
daymet_df = pd.read_csv('daymet.csv', index_col='date', parse_dates=['date'])
daymet_df.info()
#2.2: Explore this dataset and report what variables it contains, what date ranges are covered and the frequency of the data. 
daymet_df.info()
# Contains info about the year, day of year, length of day, precipitation, suns radiation, temp max and min, etc
# Dates range from 1992-09-25 to 2022-09-25
# This data is daily data
#%%
#2.3  Make a scatter plot of day length (dayl) vs maximum temperature.
fig, ax = plt.subplots()
fig.set_size_inches(15, 15)
ax.scatter(daymet_df['dayl (s)'], daymet_df['tmax (deg c)'])
ax.set_xlabel('Length of day (s)')
ax.set_ylabel('Maximum temperature (deg c)')
ax.set_title('Length of day (s) vs max temperature (deg c)')

#%%
#2.4 Make a plot with lines for the monthly average of `tmax` for all months after Jan 2015.  Add shading to the plot extending to the monthly minimum and maximum of `tmax` for the same period.
monthly_avg = daymet_df.resample('M').mean()['tmax (deg c)']
monthly_avg_2015 = monthly_avg[monthly_avg.index.year >= 2015]
max_temp = daymet_df.resample('M').max()['tmax (deg c)']
max_temp_2015 = max_temp[max_temp.index.year >= 2015]
min_temp = daymet_df.resample('M').min()['tmax (deg c)']
min_temp_2015 = min_temp[min_temp.index.year >= 2015]

ax = plt.axes()
plt.plot(monthly_avg_2015, 'o-', color = 'maroon', label = 'Mean')
plt.fill_between(max_temp_2015.index, min_temp_2015.values, max_temp_2015.values, color = 'silver', alpha=0.5, label = 'Max-Min')
ax.set_xlabel('Date')
ax.set_ylabel('Temperature (C)')
ax.legend()
plt.title('Monthly Average, Maximum, and Minimum Temperature')
# %%
mean_val = daymet_df.resample('M').mean()['tmax (deg c)']
min_val = daymet_df.resample('M').min()['tmax (deg c)']
max_val = daymet_df.resample('M').max()['tmax (deg c)']

mean_val_plot = mean_val[mean_val.index.year>=2015]
min_val_plot = min_val[min_val.index.year>=2015]
max_val_plot = max_val[max_val.index.year>=2015]

ax=plt.axes()
plt.plot(mean_val_plot, 'o-', color='blue', label='Mean')
plt.fill_between(max_val_plot.index, min_val_plot.values, max_val_plot.values, color='grey',  alpha=0.2, label='Max-Min')
ax.set_xlabel("Date")
ax.set_ylabel("Monthly Maximum daily temperature")
ax.legend()