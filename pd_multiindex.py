import numpy as np
import pandas as pd

index = [
  ("California", 2000), ("California", 2010),
  ("New York", 2000), ("New York", 2010),
  ("Texas", 2000), ("Texas", 2010)
]

populations = [
  33871648, 37253956,
  18976457, 19378102,
  20851820, 25145561
]

index = pd.MultiIndex.from_tuples(index)
pop = pd.Series(populations, index=index)
pop_df = pop.unstack()