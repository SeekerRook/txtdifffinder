#!/usr/bin/env python3
import sys
filename2 = "out.txt"
join = False
#read command line arguments
if len(sys.argv) == 1:
    print("Error: no arguments given")
    exit()
for i in range(2,len(sys.argv),2):
    if sys.argv[i] == "-o" :
        filename2 = sys.argv[i+1]

    elif sys.argv[i] == "-j" :
        filename3 = sys.argv[i+1]
        join = True
    else:
        print("Error: uncnown argument ", sys.argv[i] )
        exit()
filename1 = sys.argv[1]





#read from file
file1 = open(filename1,"r")
lines = file1.readlines()

if join :
    file3 = open(filename3,"r")
    lines3 = file3.readlines()
    lines += lines3    

print ("Calculating.....")
setofelems = {""}
for l in lines:
    setofelems.add(l)

print ("Complete")

#write to output file
file2 = open(filename2,"w")
for l in setofelems:
    file2.write(l)