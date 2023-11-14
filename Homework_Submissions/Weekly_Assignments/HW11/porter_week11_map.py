#%% 
import matplotlib.pyplot as plt
import matplotlib as mpl 
import pandas as pd 
import numpy as np
import geopandas as gpd
import fiona
from shapely.geometry import Point
import contextily as ctx

#%%
# Read in the files using geopandas
file = os.path.join('./data/gagesii_shapefile', 'gagesII_9322_sept30_2011.shp')
gages = gpd.read_file(file)

#%%
# Plot gages specifically for the state of Arizona
gages.STATE.unique() #Tells us the available states 
AZ_gages = gages[gages['STATE']=='AZ']

fig, ax = plt.subplots(figsize=(10,10))
AZ_gages.plot(ax=ax)
plt.show()

# %%
# Read in the geodataframe with the arizona watershed boundaries
file1 = os.path.join('./data/WBD_15_HU2_GDB', 'WBD_15_HU2_GDB.gdb')
#This will list all the layers in that file
fiona.listlayers(file1)
HUC6 = gpd.read_file(file1, layer="WBDHU6")

#%%
# Plot the boundary
fig, ax = plt.subplots(figsize=(10, 10))
HUC6.plot(ax=ax)
ax.set_title("HUC Boundaries")
plt.show()

# %%
# Create a list of points for the locations you want to emphasize
point_list = np.array([[-110.97688412, 32.22877495],
                       [-111.7891667, 34.44833333],
                       [-112.0740, 33.4484]])
#make these into spatial features
point_geom = [Point(xy) for xy in point_list]
point_geom

#map a dataframe of these points
point_df = gpd.GeoDataFrame(point_geom, columns=['geometry'],
                            crs=HUC6.crs)


fig, ax = plt.subplots(figsize=(10, 10))
HUC6.plot(ax=ax)
point_df.plot(ax=ax, color='red', marker='*')
ax.set_title("HUC Boundaries")
plt.show()

#%%
# Load in AZ shapefile
file2 = os.path.join('./data/arizona_shapefile', 'tl_2016_04_cousub.shp')
AZ_shape = gpd.read_file(file2)


fig, ax = plt.subplots()
AZ_shape.plot(ax=ax)
plt.show()

# %%
# Reproject into CRS coordinates so that all coordinate systems match
points_project = point_df.to_crs(AZ_gages.crs)
AZ_project = AZ_shape.to_crs(AZ_gages.crs)
HUC6_project = HUC6.to_crs(AZ_gages.crs)

# %%
# Plot reprojection to make sure it worked
fig, ax = plt.subplots(figsize=(5, 5))
AZ_gages.plot(column='DRAIN_SQKM', categorical=False,
              legend=True, markersize=45, cmap='Set2',
              ax=ax)
points_project.plot(ax=ax, color='black', marker='*')
# %%
# Combine all files to create your map
fig, ax = plt.subplots(figsize=(10, 10))
AZ_project.plot(ax=ax, zorder=1, color='lightgreen', alpha=0.5, label='Arizona State')
HUC6_project.boundary.plot(ax=ax, color=None,
                           edgecolor='black', linewidth=0.5,
                           zorder=2, label='Watershed Boundary')
ax = AZ_gages.plot(column='DRAIN_SQKM', categorical=False,
              legend=True, markersize=7, color='red',
              ax=ax, zorder=3, label='Gages')
points_project.plot(ax=ax, color='navy', marker='+', markersize=45,
                    zorder=4, label='Selected Locations')
ctx.add_basemap(ax, crs=HUC6_project.crs.to_string())
plt.legend()
plt.title('Arizona Gages and Surrounding Watershed')
# %%
