#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json 
import urllib.request as req
import urllib

# Define the Start date, end date, and site ID
start_date = '2023-11-01'
end_date = '2023-11-18'
site_id = '09506000'

def get_usgs_streamflow(site_id, start_date, end_date):
    """
    Retrieve streamflow data from USGS.

    This function will pull in our data from the USGS website.
    The parameters used for this include site ID, start_date,
    and end date which can be identified at the end of the function. 
    This is converted into a pandas dataframe that is able to
    be manipulated later on in the code.

    Parameters
    ----------
    site_id: str
        Identifier for the streamgauge site.
    start_date: str
        Start date for the data in 'YYYY-MM-DD' format.
    end_date: str
        End date for the data in 'YYYY-MM-DD' format.

    Returns
    -------
    pd.DataFrame
        Pandas DataFrame containing streamflow data.
    """
    url = f"https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no={site_id}" \
          f"&referred_module=sw&period=&begin_date={start_date}&end_date={end_date}"
    data = pd.read_table(url, skiprows=30, names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],
                         parse_dates=['datetime'], index_col=['datetime']) 
    return data['flow']  # Extract only the 'flow' column

def plot_streamflow(ax, data, label='Camp Verde Site'):
    """
    Plot streamflow data.

    Parameters
    ----------
    ax: plt.axes
        Matplotlib axes object.
    data: pd.Series
        Pandas Series containing streamflow data.
    label: str, optional
        Label for the plot.

    Returns
    -------
    plt.axes
        Matplotlib axes object.
    """
    ax.plot(data.index, data.values, color='maroon', label=label)  # Plot using index and values
    ax.tick_params(axis='x', labelrotation=45)
    ax.set_xlabel('Date')
    ax.set_ylabel('Flow')
    ax.set_title('November Streamflow Timeseries')
    ax.legend()
    return ax

def get_mesowest_precipitation():
    """
    Retrieve precipitation data from Mesowest API.

    Returns
    -------
    pd.DataFrame
        Pandas DataFrame containing precipitation data.
    """
    mytoken = 'f180791790dd4a389c123007870d3ef7'
    base_url = "http://api.mesowest.net/v2/stations/timeseries"
    args = {
        'start': '202311010000',
        'end': '202311180000',
        'obtimezone': 'UTC',
        'vars': 'precip_accum',
        'stids': 'QVDA3',
        'units': 'metric',
        'token': mytoken
    }

    api_string = urllib.parse.urlencode(args)
    full_url = f"{base_url}?{api_string}"
    response = req.urlopen(full_url)
    response_dict = json.loads(response.read())

    date_time = response_dict['STATION'][0]['OBSERVATIONS']['date_time']
    precip = response_dict['STATION'][0]['OBSERVATIONS']['precip_accum_set_1']

    data = pd.DataFrame({'Precip': precip}, index=pd.to_datetime(date_time))
    data_daily = data.resample('D').mean()
    return data_daily['Precip']  # Extract only the 'Precip' column

def plot_precipitation(ax, data, label='Precipitation'):
    """
    Plot precipitation data.

    Parameters
    ----------
    ax: plt.axes
        Matplotlib axes object.
    data: pd.Series
        Pandas Series containing precipitation data.
    label: str, optional
        Label for the plot.

    Returns
    -------
    plt.axes
        Matplotlib axes object.
    """
    ax.plot(data.index, data.values, label=label)  # Plot using index and values
    ax.tick_params(axis='x', labelrotation=45)
    ax.set_xlabel('Date')
    ax.set_ylabel('Precipitation')
    ax.set_title('November Precipitation Timeseries')
    ax.legend()
    return ax


# Retrieve and plot streamflow data
streamflow_data = get_usgs_streamflow(site_id, start_date, end_date)
ax1 = plt.subplot(2, 1, 1)  # Create subplot 1
ax1 = plot_streamflow(ax1, streamflow_data)

# Retrieve and plot precipitation data
precipitation_data = get_mesowest_precipitation()
ax2 = plt.subplot(2, 1, 2)  # Create subplot 2
ax2 = plot_precipitation(ax2, precipitation_data)

plt.tight_layout()  # Adjust layout for better spacing
plt.show()

# %%
