import numpy as np
import pandas as pd

#
rainfall = pd.read_csv("PythonDataScienceHandbook/notebooks/data/Seattle2014.csv")["PRCP"].values
inches = rainfall / 254

