# Starter code for week 6 Pandas

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week6.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)

#filepath = '../Assignments/Solutions/data/streamflow_week1.txt'

# %%
#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

#%%
#print(data)
#print(data.index)
print(data.info())
print(data.describe())
# %%
jan = data[(data.month == 1)]
print('JAN:')
jan.describe()

# %%
feb = data[(data.month == 2)]
print('FEB:')
feb.describe()

# %%
# 2. How do you get a listing of the columns in `data`?

# %%
# 3. How do you select the streamflow column in `data`?


#%%
# 5. How do you get the last streamflow value from `data`?

#%%
# 6. What is the mean streamflow value for entire period?

#%%
# 7. What is the maximum value for the entire period?

#%%
# 8. How do you find the maximum streamflow value for each year?
