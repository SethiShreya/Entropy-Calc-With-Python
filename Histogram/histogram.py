import pandas as pd
import matplotlib.pyplot as plt

def makeHistogram(df, title, xlabel, ylabel, outputFileName):
    # reading csv file from the path
    

    # plotting histogram
    plt.hist(df, bins=3)

    # Giving label to the graph
    plt.title(f"{title}")
    plt.xlabel(f"{xlabel}")
    plt.ylabel(f"{ylabel}")

    # saving histogram plt to the specifies location
    plt.savefig(f'./Histogram/{outputFileName}.png')
    # plt.show()

df= pd.read_csv("./frequency/shannon(Uniform(1_300_500)).csv")
df2= pd.read_csv("./frequency/tsallis(Uniform(1_300_500)) for q = 2.csv")
df3= pd.read_csv("./frequency/tsallis(Uniform(1_300_500)) for q = 3.csv")
df4= pd.read_csv("./frequency/tsallis(Uniform(1_300_500)) for q = 4.csv")

makeHistogram(df, "Shannon Entropy Histogram", "Shannon Entropy", "Frequency", "Shannon(Uniform(1_300_500))")
makeHistogram(df2, "Tsallis Entropy Histogram", "Tsallis Entropy for q = 2", "Frequency", "Tsallis(Uniform(1_300_500)) for q=2")
makeHistogram(df3, "Tsallis Entropy Histogram", "Tsallis Entropy for q = 3", "Frequency","Tsallis(Uniform(1_300_500)) for q=3")
makeHistogram(df4, "Tsallis Entropy Histogram",  "Tsallis Entropy for q = 4","Frequency", "Tsallis(Uniform(1_300_500)) for q=4")

