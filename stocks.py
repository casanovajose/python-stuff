import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
from keys import ALPHAVANTAGE

# historical of MELI stock
goog = web.DataReader("MELI", start="2004", end="2020", api_key=ALPHAVANTAGE, data_source="av-daily")
goog_close = goog["close"]

goog_close.index = pd.to_datetime(goog_close.index)
goog_close.plot(alpha=0.5, style="-")
goog_close.resample("BA").mean().plot(style=":")
goog_close.asfreq("BA").plot(style="--")

plt.legend(["value", "annual average", "annual end value"], loc="upper left")

plt.show()