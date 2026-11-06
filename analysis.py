import pandas as pd
import numpy as np
d = pd.read_csv("C:/Users/Arbaz/Desktop/data.csv")
x = d["harga"].sum() / 120
print(x)
