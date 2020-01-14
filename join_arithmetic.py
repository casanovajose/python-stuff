import numpy as np
import pandas as pd

df6 = pd.DataFrame({'name': ['Peter', 'Paul', 'Mary'],
'food': ['fish', 'beans', 'bread']},
columns=['name', 'food'])
df7 = pd.DataFrame({'name': ['Mary', 'Joseph'],
'drink': ['wine', 'beer']},
columns=["name", "drink"])

print(df6)
print(df7)
print(pd.merge(df6, df7))

