# Starter code for week 8 Timeseries

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week8.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)

# %%
#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=31,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

print(data)

# %%
df=data.set_index('datetime')
oct = (df.flow[(df.month >= 10) & (df.year == 2023)])
oct1 = oct.mean()
print(oct1)
oct2 = (df.flow[(df.month>= 10) & (df.year == 2023)]).describe()
# %%
week1 = oct1
print("1 Week Forecast =", week1)
week2 = oct1 - 3
print("2 Week Forecast =", week2)

# %%
fig, ax = plt.subplots(2,1)
fig.set_size_inches(17,17)
ax[0].plot(oct)
ax[0].tick_params(axis='x', labelrotation=45)
ax[1].bar(oct2.index, oct2['mean'])
ax[0].set_title('Month of October, 2023 Flow')
ax[1].set_title('Week 1 and Week 2 Forecast')
ax[0].set_ylabel('flow')
ax[1].set_ylabel('flow')
ax[0].set_xlabel('Date')
ax[1].set_xlabel('Week')
# %%
