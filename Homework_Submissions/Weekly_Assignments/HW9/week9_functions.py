# Starter code for week 9 Timeseries and Functions

# %%
# Import the modules we will use
import os
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week9.txt'
filepath = os.path.join('../../../data', filename)
print(os.getcwd())
print(filepath)

# %%
# Read the data into a pandas dataframe
dataframe = pd.read_table(filepath, sep='\t', skiprows=30,
                    names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'],
                            parse_dates=['datetime']
                    )

print(dataframe)

# %%
# Convert the dataframe into an indexed dataframe and set 
# parameters for what to keep in the dataframe for your calculation. 
# This is how to do it without creating a function
dataframe_index = dataframe.set_index('datetime')
oct = (dataframe_index.flow[(dataframe_index.index.month >= 10) & (dataframe_index.index.year == 2023)])
oct1 = oct.mean()
print(oct1)

#%%
# Create a function that will allow user to specify the month and year needed
# for the calculation of this weeks streamflow forecast.
# This does the same thing as above, but in the format of a function.
def monthly(dataframe, month):
    october_flow = (dataframe.flow[(dataframe.index.month >= month) & (dataframe.index.year == 2023)])
    return(october_flow)
my_output = monthly(dataframe = dataframe_index, month = 10)
print(my_output.mean())

# %%
# The ouput for the one week and two week streamflow forecast.
week1 = (my_output.mean()) + 13
print("1 Week Forecast =", week1)
week2 = (my_output.mean()) + 10
print("2 Week Forecast =", week2)

# %%
# Plot a figure with two plots, one showing the month of October 2023,
# the other showing the week one and two streamflow forecast in bar graph form.
fig, ax = plt.subplots(2,1)
fig.set_size_inches(20,20)
ax[0].plot(oct)
ax[0].tick_params(axis='x', labelrotation=45)
ax[1].bar(x=['week1', 'week2'], height=[week1, week2])
ax[0].set_title('Month of October, 2023 Flow')
ax[0].title.set_size(25)
ax[1].set_title('Week 1 and Week 2 Forecast')
ax[1].title.set_size(25)
ax[0].set_ylabel('flow')
ax[1].set_ylabel('flow')
ax[0].set_xlabel('Date')
ax[1].set_xlabel('Week')
# %%
