import pandas as pd
import matplotlib.pyplot as plt

# reading csv file from the path
df= pd.read_csv("./Histogram/shannon_Out.csv")

# plotting histogram
plt.hist(df)

# Giving label to the graph
plt.title("Entropy Data")
plt.xlabel("Entropy")
plt.ylabel("Frequency")

# saving histogram plt to the specifies location
plt.savefig('./Histogram/histogram.png')
# plt.show()