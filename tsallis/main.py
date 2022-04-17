import os
from math import pow
# check if the file exist in current directory
# file_exists = os.path.exists('./random_generator/Normal.csv')

sum= 0.0

# if (file_exists):
#     pass
# else:
# os.chdir("./frequency")
# print(os.getcwd())

def probabilty(string, windowsize, q):
    global sum
    n= len(string)
    count_1=0
    count_0=0
    for i in range(n):
        if string[i]=='1':
            count_1+=1
        else:
            count_0+=1

    prob_0= pow(count_0/windowsize, q)
    prob_1= pow(count_1/windowsize, q)
    prob_0_1 = prob_0+ prob_1
    s= (1/(q-1))*(1-prob_0_1)
    sum=sum+s
    return s
   

# reading content of file
with open("./tsallis/input.csv") as f:
    # print(f.read())
    string= f.read()


# taking input of window size  
n= len(string)
countentropy=0
no_of_entropy= int(input("How many entropy you want: "))
# w= int(input("Enter the window size: "))
w= n-(no_of_entropy-1)
size=w
print("Size of Window will be "+str(w))
power= 2
for i in range(n):
    if i+w>n:
        break
    countentropy+=1
count=0

for j in range(2, 5):
    # will open 3 files for q= 1,2,3 and store output 
    with open(f"./tsallis/output for q = {j}.csv", 'w') as wr:
        for i in range(countentropy):
            wr.write(str(probabilty(string[i:w], size, j))+"\n")
        wr.write(f'\n\nThe average is {sum/countentropy}\n\n')
        sum = 0.0
# print(countentropy)