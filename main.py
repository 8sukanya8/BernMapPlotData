from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as p

# Set your working directory here
DIR= "/Users/sukanyanath/PycharmProjects/"

# Create a Basemap object setting the coordinates around the box surrounding area of Bern Canton
map = Basemap(llcrnrlon=6.68, llcrnrlat=46.3, urcrnrlon=8.7, urcrnrlat=47.32,
              resolution='i', projection='tmerc', lat_0=39.5, lon_0=1)

# Draw boundaries, coastlines and map background
map.drawcountries(linewidth=0.5, linestyle='solid', color='black', antialiased=1, ax=None, zorder=None)
map.drawcoastlines()
map.shadedrelief()

# Add shapes of districts and cantons of Switzerland
shapefile2= DIR + "BernMapPlotData/CHE_adm_shp/CHE_adm2"
shapefile1= DIR + "BernMapPlotData/CHE_adm_shp/CHE_adm1"

map.readshapefile(shapefile2, name="areas", drawbounds=True, zorder=None, linewidth=0.5, color='gray', antialiased=1, ax=None, default_encoding='utf-8')
map.readshapefile(shapefile1, name="areas", drawbounds=True, zorder=None, linewidth=0.5, color='black', antialiased=1, ax=None, default_encoding='utf-8')

# Read the data from Amtsbezirke_Bern.csv.
data = p.read_csv(DIR+"BernMapPlotData/Amtsbezirke_Bern.csv").values
lat = list(data[:,1])
lon = list(data[:,2])
value = list(data[:,3])

# Plot the data
map.scatter(lon, lat, latlon=True,
          c=value, s=value,
          cmap='Reds', alpha=0.5)

plt.colorbar(label=r'value') # Replace with parameter name
plt.clim(10, 100)

# Draw labels and measurement bars
for a in [10, 25, 50, 75]: # Replace with the parameter involved
    plt.scatter([], [], c='red', alpha=1, s=a,
                label=str(a) + ' metric')
plt.legend(scatterpoints=1, frameon=False,
           labelspacing=1, loc='lower left')

# Time for the show
plt.show()

