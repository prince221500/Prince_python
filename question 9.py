# Write a Python program to read a random line from a file.
import random as r
f=open("kshitiz.txt","r")
x=f.readlines()
rs=r.randint(0,len(x)-1)
print(x[rs])