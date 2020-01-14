import pandas as pd
import numpy as np

def make_df(cols, ind):
  """Quick DF Maker"""
  data = {c: [str(c) + str(i) for i in ind]
          for c in cols}
  return pd.DataFrame(data, ind);
