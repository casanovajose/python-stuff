import numpy as np
import pandas as pd

index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]],
                                     names=["year", "visit"])

columns = pd.MultiIndex.from_product([["Bob", "Guido", "Sue"], ["HR", "Temp"]],
                                      names=["subject", "type"])

data = np.round(np.random.rand(4, 6), 1)
data[:, ::2] *= 10