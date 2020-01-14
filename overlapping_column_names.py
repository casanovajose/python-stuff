import numpy as np
import pandas as pd

df8 = pd.DataFrame({"name": ["Bob", "Jake", "Lisa", "Sue"],
"rank": [1, 2, 3, 4]})
df9 = pd.DataFrame({"name": ["Bob", "Jake", "Lisa", "Sue"],
"rank": [3, 1, 4, 2]})

print(df8); print(df9)
print("---merge adding suffixes on overlapped columns")
print(pd.merge(df8, df9, on="name", suffixes=["_L", "_R"]))