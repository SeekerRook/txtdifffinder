import sys
import os

filename1 = input("Give Input File:")
filename2 = input("Give Output File (Enter for default):")
if filename2 == "" : filename2 = "out.txt"
filename3 ="/"
joinl =[]
join = False
while filename3 != "" :

        filename3 = input("Give Input File to join (ENTER to stop):")
        if filename3 != "":
            joinl.append(filename3)
if len(joinl) > 1: join = True

print(joinl)
#read from file
if os.path.exists(os.path.join(filename1)):
    file1 = open(filename1,"r")
    lines = file1.readlines()
else: 
    print("Error: invalid file ", filename1)
    exit()
if join :
    for filename3 in joinl:
        if os.path.exists(os.path.join(filename3)):
            file3 = open(filename3,"r")
            lines3 = file3.readlines()
            lines += lines3    
        else:
            print("Error: invalid file ", filename3)
            exit()
print ("Calculating.....")
setofelems = {""}
for l in lines:
    setofelems.add(l)

print ("Complete")

#write to output file
file2 = open(filename2,"w")
for l in setofelems:
    file2.write(l)