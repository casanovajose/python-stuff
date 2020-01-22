import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
from keys import ALPHAVANTAGE

# historical of MELI stock
company = web.DataReader("MELI", start="2004", end="2020", api_key=ALPHAVANTAGE, data_source="av-daily")
company = company["close"]
company.index = pd.to_datetime(company.index)

# company = company.asfreq("D", method="pad")

rolling = company.rolling(365, center=True)

data = pd.DataFrame({
  "input": company,
  "one-year rolling_mean": rolling.mean(),
  "one-year rolling_std": rolling.std()
})

ax = data.plot(style=["-", "--", ":"])
ax.lines[0].set_alpha(0.3)

plt.show()