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
sum_shannon=0
sum_tsallis=0

def shannon(freq, size):
    prob= freq/size
    return abs(-(prob*(log2(prob))))

def tsallis(freq, size, q):
    prob= pow(freq/size, q)
    return (1/(q-1))*(1-prob)

def frequency(listob):
    size= len(listob)
    q=2
    global sum_shannon
    global sum_tsallis
    freq = count(listob)
    # for shannon
    with open("./frequency/shannon(Uniform(1_300_500)).csv", 'w') as shan:
        for i in freq:
            # shan.write(f"Shannon entropy of {i} is {str(shannon(freq[i], size))}\n")
            # tsal.write(f"Tsallis entropy of {i} is {str(tsallis(freq[i], size, q))}\n")
            s= shannon(freq[i], size)
            sum_shannon+=s
            shan.write(str(s)+'\n')
               
    # for tsallis
    for i in range(2, 5):
        with open(f"./frequency/tsallis(Uniform(1_300_500)) for q = {i}.csv", 'w') as tsal:
            for j in freq:
                st = tsallis(freq[j], size, i)
                sum_tsallis+=st
                tsal.write(str(st)+'\n')
            


inplist = []
# with open("input.csv") as f:
with open("./random_generator/Uniform(1_300_500).csv") as f:
    csvread= csv.reader(f)

    for line in csvread:
        element = ''.join(line)
        inplist.append(element)
frequency(inplist)

with open("./frequency/shannon(Uniform(1_300_500)).csv", 'a') as f:
    f.write("\n\n\n\nAverage: ")
    f.write(str(sum_shannon/len(inplist)))

for i in range(2, 5):
    with open(f"./frequency/tsallis(Uniform(1_300_500)) for q = {i}.csv", 'a') as file:
        file.write("\n\n\n\nAverage: ")
        file.write(str(sum_tsallis/len(inplist)))


