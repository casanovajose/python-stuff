import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
from keys import ALPHAVANTAGE

# historical of MELI stock
company = web.DataReader("MELI", start="2004", end="2020", api_key=ALPHAVANTAGE, data_source="av-daily")
company = company["close"]
company.index = pd.to_datetime(company.index)
company = company.asfreq("D", method="pad")

fig, ax = plt.subplots(3, sharey=True)

company.plot(ax=ax[0])
company.shift(900).plot(ax=ax[1])
company.tshift(900).plot(ax=ax[2])

local_max = pd.to_datetime("2007-11-05")
offset = pd.Timedelta(900, "D")

ax[0].legend(["input"], loc=2)
ax[0].get_xticklabels()[4].set(weight="heavy", color="red")
ax[0].axvline(local_max, alpha=0.3, color="red")

ax[1].legend(["shift(900)"], loc=2)
ax[1].get_xticklabels()[4].set(weight="heavy", color="red")
ax[1].axvline(local_max + offset, alpha=0.3, color="red")

ax[2].legend(["tshift(900)"], loc=2)
ax[2].get_xticklabels()[1].set(weight="heavy", color="red")
ax[2].axvline(local_max + offset, alpha=0.3, color="red");

plt.show()

# return on investment
# roi = 100 * (company.tshift(-365) / company - 1)
# roi.plot()
# plt.ylabel("% Return on Investment")