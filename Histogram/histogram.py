import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

def makeHistogram(df, title, xlabel, ylabel, outputFileName):
    # reading csv file from the path
    

    # plotting histogram
    plt.hist(df)

    # Giving label to the graph
    plt.title(f"{title}")
    plt.xlabel(f"{xlabel}")
    plt.ylabel(f"{ylabel}")

    # saving histogram plt to the specifies location
    plt.savefig(f'./Histogram/{outputFileName}.png')
    # plt.show()

# df= pd.read_csv("./frequency/random_numbers_decimal_edition_Shannon_Output.csv")
# # df2= pd.read_csv("./Histogram/output(500_windowsize_167771661).csv")
# # df3= pd.read_csv("./tsallis/BimaryEquivalentOutput for q = 4 with windowSize_32061.csv")
# df2= pd.read_csv("./frequency/tsallis(random_numbers_decimal_edition) for q = 2.csv")
# df3= pd.read_csv("./frequency/tsallis(random_numbers_decimal_edition) for q = 3.csv")
# df4= pd.read_csv("./frequency/tsallis(random_numbers_decimal_edition) for q = 4.csv")

# makeHistogram(df, "Shannon Entropy Histogram", "Shannon Entropy", "Frequency", "Shannon(random_numbers_decimal_edition_Shannon_Output)")
# makeHistogram(df2, "Tsallis Entropy Histogram",  "Tsallis Entropy for q = 2","Frequency", "Tsallis(random_numbers_decimal_edition) for q=2")
# makeHistogram(df3, "Tsallis Entropy Histogram",  "Tsallis Entropy for q = 3","Frequency", "Tsallis(random_numbers_decimal_edition) for q=3")
# makeHistogram(df4, "Tsallis Entropy Histogram",  "Tsallis Entropy for q = 4","Frequency", "Tsallis(random_numbers_decimal_edition) for q=4")


# df= pd.read_csv("./Histogram/freq.csv")
# column2 = df.iloc[:,1]
# print(column2)

df= pd.read_csv("./Histogram/freq.csv")
sb.histplot(df)
plt.show()