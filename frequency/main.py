import csv
from math import log2
import os
from collections import Counter as count
# check if the file exist in current directory
# file_exists = os.path.exists('./random_generator/Normal.csv')

# if (file_exists):
#     pass
# else:
# os.chdir("./frequency")
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
    with open("./frequency/shannon.csv", 'w') as shan:
        with open("./frequency/tsallis.csv", 'w') as tsal:
            for i in freq:
                # shan.write(f"Shannon entropy of {i} is {str(shannon(freq[i], size))}\n")
                # tsal.write(f"Tsallis entropy of {i} is {str(tsallis(freq[i], size, q))}\n")
                shan.write(str(shannon(freq[i], size))+'\n')
                tsal.write(str(tsallis(freq[i], size, q))+'\n')


inplist = []
with open("./random_generator/Normal.csv") as f:
    csvread= csv.reader(f)

    for line in csvread:
        element = ''.join(line)
        inplist.append(element)
frequency(inplist)


