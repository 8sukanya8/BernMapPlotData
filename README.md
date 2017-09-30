# Plot Data on Bern Canton Map by districts
Data visualisation on a map appeals to the eye. Here is one way in which you can do it.
![Fig](figure_1.png?raw=true)

## 1 - How to use this code?
**Step 1:** Set working directory on line 6 of main.py

**Step 2:** Replace the values column in **AmtsBezirke_Bern.csv** with the parameter values that you want

**Step 3:** [Optional but recommended] Replace the label name of the parameter name on line 35 of main.py

**Step 4:** [Optional but recommended] Replace the metric and measurements on line 39 of main.py

# 2 - How to create your own map for some other region or country
**Step 1:** Find the bounding box representing the region/country you wanted to cover here. Use option "csv". Use these parameters to set the map object on line 9.
[BoundingBox](http://boundingbox.klokantech.com)


**Step 2:** View the docs of basemap and matplotlib for tuning the parameters
[matplotlib](https://matplotlib.org/api/)
[basemap](http://basemaptutorial.readthedocs.io/en/latest/)

**Step 3:** Find Shapefiles for the country or region desired. Here I used the following link for Switzerland
[opendata.swiss](https://opendata.swiss/en/dataset/swissboundaries3d-gemeindegrenzen1)

**Step 4:** If you do not have latitudes and longitudes, you may use gpsvisualizer and mapquest for geo coding the regions
[gpsvisualizer](http://www.gpsvisualizer.com/geocoder/)
[mapquest](https://developer.mapquest.com)
Save the geocoded file with parameter values as desired. Update file read information on line 25 of main.py

**Step 5:** Follow the steps mentioned in [How to use this code](#1---how-to-use-this-code)