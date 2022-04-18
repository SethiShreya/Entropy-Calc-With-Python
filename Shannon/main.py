from math import log2
import os
# check if the file exist in current directory
# file_exists = os.path.exists('input.csv')

# if (file_exists):
#     pass
# else:
#     os.chdir("./Shannon")
# print(os.getcwd())


def entropy(string,size):
    n= len(string)
    count=0
    for i in range(n):
        if string[i]=='1':
            count+=1

    return abs(-(count/size)*(log2(count/size)))
   


with open("./Shannon/BinaryEquivalent.csv") as f:
    # print(f.read())
    string= f.read()


    
n= len(string)
countentropy=0
no_of_entropy= int(input("How many entropy you want: "))
# w= int(input("Enter the window size: "))
w= n-(no_of_entropy-1)
size=w
print("Size of Window will be "+str(w))
for i in range(n):
    if i+w>n:
        break
    countentropy+=1
count=0
with open(f"./Shannon/BinaryEquivalentOutput with WindowSize_{w}.csv", 'w') as wr:
    for i in range(countentropy):
        wr.write(str(entropy(string[i:w], size))+"\n")
        w+=1

# print(countentropy)