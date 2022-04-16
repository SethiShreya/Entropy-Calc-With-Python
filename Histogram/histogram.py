import pandas as pd
import matplotlib.pyplot as plt

def makeHistogram(df, title, xlabel, ylabel, outputFileName):
    # reading csv file from the path
    

    # plotting histogram
    plt.hist(df, bins=7)

    # Giving label to the graph
    plt.title(f"{title}")
    plt.xlabel(f"{xlabel}")
    plt.ylabel(f"{ylabel}")

    # saving histogram plt to the specifies location
    plt.savefig(f'./Histogram/{outputFileName}.png')
    # plt.show()

df= pd.read_csv("./frequency/shannon.csv")
df2= pd.read_csv("./frequency/tsallis for q = 2.csv")
df3= pd.read_csv("./frequency/tsallis for q = 3.csv")
df4= pd.read_csv("./frequency/tsallis for q = 4.csv")

makeHistogram(df, "Shannon Entropy Histogram", "Frequency", "Shannon Entropy", "Shannon")
makeHistogram(df2, "Tsallis Entropy Histogram", "Frequency", "Tsallis Entropy for q = 2", "Tsallis for q=2")
makeHistogram(df3, "Tsallis Entropy Histogram", "Frequency", "Tsallis Entropy for q = 3", "Tsallis for q=3")
makeHistogram(df4, "Tsallis Entropy Histogram", "Frequency", "Tsallis Entropy for q = 4", "Tsallis for q=4")

