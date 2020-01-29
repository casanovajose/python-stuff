import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
cities = pd.read_csv("data/california_cities.csv")

# extract some data
lat, lon = cities["latd"], cities["longd"]
population, area = cities["population_total"], cities["area_total_km2"]

plt.scatter(lon, lat, label=None,
     c=np.log10(population), cmap="viridis",
     s=area, linewidth=0, alpha=0.5)
plt.axis(aspect="equal")
plt.xlabel("longitud")
plt.ylabel("latitud")
plt.colorbar(label="log$_{10}$(population)")
plt.clim(3, 7)

# empty list for plotting the legends
for area in [100, 300, 500]:
    plt.scatter([],[], c="k", alpha=0.3, s=area, label=str(area) + " km$^2$")

plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title="Area de la ciudad")

plt.title("Ciudades de California: área y población")
plt.show()