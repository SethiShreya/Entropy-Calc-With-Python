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
    count_0=0
    count_1=0
    for i in range(n):
        if string[i]=='1':
            count_1+=1
        else:
            count_0+=1

    ent_1 = abs(-(count_1/size)*(log2(count_1/size)))
    ent_0 = abs(-(count_0/size)*(log2(count_0/size)))
    return ent_1+ent_0


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
total=0
with open(f"./Shannon/BinaryEquivalentOutput with windowsize={w}.csv", 'w') as wr:
    for i in range(countentropy):
        s=entropy(string[i:w], size)
        total+=s
        wr.write(str(s)+"\n")
        w+=1
print(countentropy)
with open(f"./Shannon/BinaryEquivalentOutput with windowsize=31961.csv", 'a') as wr:
    wr.write(f"\n\nAverage is {total/countentropy}")
# print(countentropy)