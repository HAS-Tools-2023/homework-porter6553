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
filename = 'streamflow_week7.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)

#filepath = '../Assignments/Solutions/data/streamflow_week1.txt'

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
monthly_avg1 = data.groupby(['month'])[['flow']].describe()
monthly_avg1
monthly_avg1.columns = monthly_avg1.columns.droplevel(0)
f, ax = plt.subplots()
ax.bar(monthly_avg1.index, monthly_avg1['mean'], color='maroon', label='Monthly Average')
ax.legend()
ax.set_xlabel('Month')
ax.set_ylabel('Flow in cfs')
ax.set_title('Monthly Average Flow')

# %%
#Plot 1 for the data
monthly_avg2 = data.groupby(data.month)["flow"].mean()
fig, axes  = plt.subplots(2,1)
fig.set_size_inches(10,11)
#ax = plt.axes()
#ax.scatter(x=data.year, y=data.flow, c=data.month, color='Spectral')
data.plot.scatter(x='year', y='flow', c='month', colormap='Spectral', ax=axes[0])
monthly_avg2.plot(ax=axes[1], label='Average Flow')
axes[1].set_ylabel('flow')
axes[0].set_title('Monthly Stream Flow by Year in cfs')
axes[1].set_title('Average Flow by Month in cfs')
axes[1].legend()
#axes[1].plot(monthly_avg)

# %%
df = data.set_index('datetime')
print(df)
oct = (df.flow[(df.month >= 10) & (df.year == 2023)])
plt.plot(oct, label="Daily Flow")
plt.xticks(rotation=45, ha="right")
plt.xlabel("Date")
plt.ylabel("Flow in cfs")
plt.title("October 2023 Daily Flow")
plt.legend()
# %%
week = (df.flow[(df.month>=10) & (df.year == 2023) & (df.day>=8) & (df.day<=14)])
plt.plot(week, label="Week Flow")
plt.xticks(rotation=45, ha='right')
plt.xlabel("Date")
plt.ylabel("Flow in cfs")
plt.legend()
plt.title("Flow for the week of October 8-14, 2023")
# %%
plt.bar(data.month, data.flow, label="Flow by month")
plt.plot(monthly_avg1.index, monthly_avg1['mean'], color='red', label="Monthly average")
plt.xlabel("Month")
plt.ylabel("flow in cfs")
plt.legend()
plt.title("Total flow and average flow by month")
# %%
