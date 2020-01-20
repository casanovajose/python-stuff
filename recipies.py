import numpy as np
import pandas as pd
import re

# read the entire file into a Python array
with open("recipies/recipeitems-latest.json", "r") as f:
# Extract each line
  data = (line.strip() for line in f)
# Reformat so each line is the element of a list
  data_json = "[{0}]".format(','.join(data))
# read the result as a JSON
recipes = pd.read_json(data_json)

spice_list = ['salt', 'pepper', 'oregano', 'sage', 'parsley',
'rosemary', 'tarragon', 'thyme', 'paprika', 'cumin']

spice_df = pd.DataFrame(
           dict((spice, recipes.ingredients.str.contains(spice, re.IGNORECASE)) for spice in spice_list)
)

# make a query
selection = spice_df.query("parsley & paprika & tarragon")
print(len(selection))

print(selection.head())