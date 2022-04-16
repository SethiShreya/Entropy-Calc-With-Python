import csv
from math import log2
import os
from collections import Counter as count
# check if the file exist in current directory
# file_exists = os.path.exists('input.csv')

# if (file_exists):
#     pass
# else:
#     os.chdir("./frequency")
# print(os.getcwd())

def shannon(freq, size):
    prob= freq/size
    return abs(-(prob*(log2(prob))))

def tsallis(freq, size, q):
    prob= pow(freq/size, q)
    return (1/(q-1))*(1-prob)

def frequency(listob):
    size= len(listob)
    q=2
    freq = count(listob)
    # for shannon
    with open("./frequency/shannon.csv", 'w') as shan:
        for i in freq:
            # shan.write(f"Shannon entropy of {i} is {str(shannon(freq[i], size))}\n")
            # tsal.write(f"Tsallis entropy of {i} is {str(tsallis(freq[i], size, q))}\n")
            shan.write(str(shannon(freq[i], size))+'\n')
               
    # for tsallis
    for i in range(2, 5):
        with open(f"./frequency/tsallis for q = {i}.csv", 'w') as tsal:
            for j in freq:
                tsal.write(str(tsallis(freq[j], size, i))+'\n')
            


inplist = []
# with open("input.csv") as f:
with open("./random_generator/Triangular.csv") as f:
    csvread= csv.reader(f)

    for line in csvread:
        element = ''.join(line)
        inplist.append(element)
frequency(inplist)


