#!/usr/bin/env python3
import sys
import os
filename2 = "out.txt"
join = False
joinl = []
#read command line arguments
if len(sys.argv) == 1:
    print("Error: no arguments given")
    exit()
for i in range(2,len(sys.argv),2):
    if sys.argv[i] == "-o" :
        filename2 = sys.argv[i+1]

    elif sys.argv[i] == "-j" :
        joinl.append(sys.argv[i+1])
        join = True
    else:
        print("Error: uncnown argument ", sys.argv[i] )
        exit()
filename1 = sys.argv[1]





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