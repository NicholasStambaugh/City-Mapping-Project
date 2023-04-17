import osmnx as ox
import pandas as pd

city = input("Enter a city name: ")
place = [city]
gdf_nodes = gdf_edges = None
for place in place:
    G = ox.graph_from_place(place, retain_all=True, simplify=True, network_type='walk')
    n_, e_ = ox.graph_to_gdfs(G)
    n_["place"] = place
    e_["place"] = place
    if gdf_nodes is None:
        gdf_nodes = n_
        gdf_edges = e_
    else:
        gdf_nodes = pd.concat([gdf_nodes, n_])
        gdf_edges = pd.concat([gdf_edges, e_])

#Plot it !
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

colors = {'Grand Rapids': 'red'}
fig = gdf_edges.plot(column="place", cmap=ListedColormap([colors[k] for k in sorted(colors.keys())]), figsize=(10, 10),
alpha=1, linewidth=0.7, edgecolor='red')# Setting the line color to blue and the background to orange
fig.set_facecolor('black')


plt.title(city)
plt.xticks([])
plt.yticks([])
fig.spines['top'].set_visible(False)
fig.spines['right'].set_visible(False)
fig.spines['bottom'].set_visible(False)
fig.spines['left'].set_visible(False)
plt.show()

plt.savefig("GR.jpg", dpi=600, format="jpg")