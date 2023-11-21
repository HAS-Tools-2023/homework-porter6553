#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os

#%%
# Make a function that will get the streamflow from the URL and read it
def get_streamflow(siteID, start_date, end_date):
    url1 = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=" + siteID + \
      "&referred_module=sw&period=&begin_date=" + start_date + "&end_date=" + end_date
    data = pd.read_table(url1, skiprows=30, names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'], parse_dates=['datetime'], index_col=['datetime']) 
    return data
# %%
# Define the Start date, end date, and site ID
start = '2023-11-01'
end = '2023-11-18'

site = get_streamflow(siteID = '09506000', start_date = start, end_date = end)

#%%
# Plot the site 
ax = plt.axes()
ax.plot(site['flow'], color= 'maroon', label = 'Camp Verde Site')
ax.tick_params(axis='x', labelrotation=45)
ax.set_xlabel('Date')
ax.set_ylabel('Flow')
ax.set_title('November Streamflow Timeseries')
ax.legend()

# %%
#Pull data from new source
mytoken = 'f180791790dd4a389c123007870d3ef7'
base_url = "http://api.mesowest.net/v2/stations/timeseries"
args = {
    'start': '202311010000',
    'end': '202311180000',
    'obtimezone': 'UTC',
    'vars': 'precip_accum',
    'stids': 'QVDA3',
    'units': 'metric',
    'token': mytoken} 

apiString = urllib.parse.urlencode(args)
fullUrl = base_url + '?' + apiString
response = req.urlopen(fullUrl)
responseDict = json.loads(response.read())

dateTime = responseDict['STATION'][0]['OBSERVATIONS']['date_time']
precip = responseDict['STATION'][0]['OBSERVATIONS']['precip_accum_set_1']

# Now we can combine this into a pandas dataframe
data = pd.DataFrame({'Precip': precip}, index=pd.to_datetime(dateTime))
data_daily = data.resample('D').mean()

ax = plt.axes()
ax.plot(data_daily, label = 'Precipitation')
ax.tick_params(axis='x', labelrotation=45)
ax.set_xlabel('Date')
ax.set_ylabel('Precip')
ax.set_title('November Precipitation Timeseries')
ax.legend()
# %%
