from math import log2
import os
os.chdir(".\Shannon")
print(os.getcwd())


def entropy(string,size):
    n= len(string)
    count=0
    for i in range(n):
        if string[i]=='1':
            count+=1

    return abs(-(count/size)*(log2(count/size)))
   


with open("input.csv") as f:
    # print(f.read())
    string= f.read()


    
n= len(string)
countentropy=0
# w= int(input("Enter the window size: "))
w= n-99
size=w
for i in range(n):
    if i+w>n:
        break
    countentropy+=1
count=0
with open("output.csv", 'w') as wr:
    for i in range(countentropy):
        wr.write(str(entropy(string[i:w], size))+"\n")
        w+=1

# print(countentropy)