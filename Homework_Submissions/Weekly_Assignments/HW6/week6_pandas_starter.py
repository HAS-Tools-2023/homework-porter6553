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
mar = data[(data.month == 3)]
print('MARCH:')
mar.describe()

# %%
apr = data[(data.month == 4)]
print('APRIL:')
apr.describe()

#%%
may = data[(data.month == 5)]
print('MAY:')
may.describe()

#%%
june = data[(data.month == 6)]
print('JUNE:')
june.describe()

#%%
july = data[(data.month == 7)]
print('JULY:')
july.describe()

#%%
aug = data[(data.month == 8)]
print('AUG:')
aug.describe()

# %%
sep = data[(data.month == 9)]
print('SEP:')
sep.describe()
# %%
oct = data[(data.month == 10)]
print('OCT:')
oct.describe()
# %%
nov = data[(data.month == 11)]
print('NOV:')
nov.describe()
# %%
dec = data[(data.month == 12)]
print('DEC:')
dec.describe()
# %%
data.sort_values(by='flow', ascending = True)
data.sort_values(by='flow', ascending = False)

#%%
val1 = 115 + ((115 * 0.1) / 2)
val2 = 115 - ((115 * 0.1) / 2)
print(val1,val2)
#%%
historicaldates = (data[(data.flow >= 109.25) & (data.flow <= 120.75) & (data.month == 9)])
print("Historial Dates:")
historicaldates.sort_values(by='datetime', ascending = True)
print(historicaldates.shape)
#%%
recentflow = (data[(data.month >= 9) & (data.year == 2023)])
print(recentflow)
#%%
octflow1 = (data.flow[(data.month == 10) & (data.year >= 2010) & (data.day >= 1) & (data.day <= 7)])
print(octflow1)
#%%
octflow2 = (data.flow[(data.month == 10) & (data.year >= 2010) & (data.day >= 8) & (data.day <= 15)])
print(octflow2)
#%%
octflow3 = (data.flow[(data.month == 10) & (data.year >= 2010) & (data.day >= 16) & (data.day <= 22)])
print(octflow3)
#%%
octflow4 = (data.flow[(data.month == 10) & (data.year == 2023) & (data.day >= 1) & (data.day <= 7)])
print(octflow4)
#%%
print('oct1-7currentavg:', np.mean(octflow4))
print('oct1-7avg:', np.mean(octflow1))
print('oct8-15avg:', np.mean(octflow2))
print('oct16-22avg:', np.mean(octflow3))

#%%
fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, 1, figsize = (20,25))
ax1.set_ylim(30,200)
ax2.set_ylim(30,200)
ax3.set_ylim(30,200)
ax4.set_ylim(30,200)
ax5.set_ylim(30,200)

ax1.plot(octflow1, color = 'b')
ax1.grid(which = 'major', linestyle = '-', alpha = 0.5)

ax2.plot(octflow2, color = 'r')
ax2.grid(which = 'major', linestyle = '-', alpha = 0.5)

ax3.plot(octflow3, color = 'g')
ax3.grid(which = 'major', linestyle = '-', alpha = 0.5)

ax4.plot(octflow4, color = 'orange')
ax4.grid(which = 'major', linestyle = '-', alpha = 0.5)

ax5.plot(recentflow, color = 'y')
ax5.grid(which = 'major', linestyle = '-', alpha = 0.5)
# %%
