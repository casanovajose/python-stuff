import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
from keys import ALPHAVANTAGE

# historical of MELI stock
company = web.DataReader("MELI", start="2004", end="2020", api_key=ALPHAVANTAGE, data_source="av-daily")
company_close = company["close"]

company_close.index = pd.to_datetime(company_close.index)
company_close.plot(alpha=0.5, style="-")
company_close.resample("BA").mean().plot(style=":")
company_close.asfreq("BA").plot(style="--")

plt.legend(["value", "annual average", "annual end value"], loc="upper left")

plt.show()