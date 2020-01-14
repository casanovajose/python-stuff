import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()

births = pd.read_csv("cdc/births.csv")
births["decade"] = 10 * (births["year"] // 10)
births_decade_gender = births.pivot_table("births", index="decade", columns="gender", aggfunc="sum")

births_year_gender = births.pivot_table("births", index="year", columns="gender", aggfunc="sum")
births_year_gender.plot()
plt.ylabel("Total births per year")