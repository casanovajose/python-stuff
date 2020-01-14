import seaborn as sns
planets = sns.load_dataset("planets");

print("grouping <groupby> objects")

for (method, group) in planets.groupby("method"):
  print("{0:30s} shape={1}".format(method, group.shape))

planets.groupby("method")