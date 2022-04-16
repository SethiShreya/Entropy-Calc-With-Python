import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv("./Histogram/shannon_Out.csv")

plt.hist(df)
plt.savefig('./Histogram/histogram.png')
# plt.show()