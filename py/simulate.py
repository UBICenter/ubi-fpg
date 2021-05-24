import pandas as pd
import numpy as np
import microdf as mdf

c = pd.read_csv("../data/asec_2019_ipums.csv.gz")
c.columns = c.columns.str.lower()


