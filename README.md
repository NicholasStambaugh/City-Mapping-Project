# The City Mapping Project

This is a Python script that uses the OSMnx library to map a city's road network. I plan to map as many cities as possible, whenever I feel like it.


# Usage
1. Install the required libraries: osmnx and pandas

2. Run the script using a Python interpreter

3. Enter the name of the city that you want to map

4. The script will generate a map of the city's road network using OSMnx


# How it works
The user enters the name of a city

The script uses the OSMnx graph_from_place function to retrieve the road network for the specified city

The graph_to_gdfs function is used to convert the road network into GeoDataFrames for nodes and edges

The place column is added to each GeoDataFrame to specify the city name

The GeoDataFrames are combined to create a single GeoDataFrame for nodes and edges

The plot function from the geopandas library is used to plot the road network

The color of the road network is set to red for the specified city

The background of the plot is set to black

The city name is added as the title of the plot

The axes and spines of the plot are hidden to provide a cleaner look

# Dependencies
osmnx
pandas
matplotlib
geopandas

# Acknowledgements
This script uses the OSMnx library, which is built on top of NetworkX and GeoPandas. OSMnx was developed by Geoff Boeing and is licensed under the MIT License.
