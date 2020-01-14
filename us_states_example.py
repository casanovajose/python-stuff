import numpy as np
import pandas as pd
import numexpr as ne

pop = pd.read_csv("us-states/state-population.csv")
areas = pd.read_csv("us-states/state-areas.csv")
abbrevs = pd.read_csv("us-states/state-abbrevs.csv")

print(pop.head())
print(areas.head())
print(abbrevs.head())

# get the abbrev
merged = pd.merge(pop, abbrevs, how="outer", left_on="state/region", right_on="abbreviation")
# drop duplicate info
merged = merged.drop("abbreviation", 1)
merged.head()
print("----")
print(merged)
print(merged.loc[merged["state"].isnull(), "state/region"].unique())
print("PR and USA are null we fill")

merged.loc[merged["state/region"] == "PR", "state"] = "Puerto Rico"
merged.loc[merged["state/region"] == "USA", "state"] = "United States"
print(merged.isnull().any())

final = pd.merge(merged, areas, on="state", how="left")
print(final)
print(final.isnull().any())

final.dropna(inplace=True)
# recommended to use with numexpr
data2010 = final.query("year == 2010 & ages == 'total'")
print(data2010.head())

data2010.set_index("state", inplace=True)
density = data2010["population"] / data2010["area (sq. mi)"]

density.sort_values(ascending=False, inplace=True)
print(density)