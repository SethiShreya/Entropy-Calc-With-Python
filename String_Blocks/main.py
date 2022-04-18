import csv
from math import log2
import os
from collections import Counter as count
# check if the file exist in current directory
# file_exists = os.path.exists('input.csv')

# if (file_exists):
#     pass
# else:
#     os.chdir("./String_Blocks")
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
    with open("./String_Blocks/freq.csv", 'w') as fr:
        for i in freq:
            fr.write(f"{i},{freq[i]}\n")
    
    # for shannon
    # with open("./String_Blocks/input.csv", 'w') as shan:
    #     for i in freq:
    #         # shan.write(f"Shannon entropy of {i} is {str(shannon(freq[i], size))}\n")
    #         # tsal.write(f"Tsallis entropy of {i} is {str(tsallis(freq[i], size, q))}\n")
    #         s= shannon(freq[i], size)
    #         sum_shannon+=s
    #         shan.write(str(s)+'\n')
               
    # for tsallis
    # for i in range(2, 5):
    #     with open(f"./String_Blocks/tsallis(random_numbers_decimal_edition) for q = {i}.csv", 'w') as tsal:
    #         for j in freq:
    #             st = tsallis(freq[j], size, i)
    #             sum_tsallis+=st
    #             tsal.write(str(st)+'\n')
            


inplist = []
# with open("input.csv") as f:
with open("./String_Blocks/Uniform(1_100_300).csv") as f:
    csvread= csv.reader(f)

    for line in csvread:
        element = ''.join(line)
        inplist.append(element)
frequency(inplist)

# with open("./String_Blocks/random_numbers_decimal_edition_Shannon_Output.csv", 'a') as f:
#     f.write("\n\n\n\nAverage: ")
#     f.write(str(sum_shannon/len(inplist)))

# for i in range(2, 5):
#     with open(f"./String_Blocks/tsallis(random_numbers_decimal_edition) for q = {i}.csv", 'a') as file:
#         file.write("\n\n\n\nAverage: ")
#         file.write(str(sum_tsallis/len(inplist)))


