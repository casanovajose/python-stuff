# nice
import numpy as np

def bogosort(x):
  while np.any(x[:-1] > x[1:]):
    np.random.shuffle(x)
  return x