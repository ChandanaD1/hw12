# normal distribution

import pandas as pd
import plotly.figure_factory as ff 
import csv

df = pd.read_csv("rating.csv")
rating = df["Avg Rating"].tolist()

graph = ff.create_distplot([rating],["Average Ratings"])
graph.show()