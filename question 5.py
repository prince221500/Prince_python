# Write a python program to find the longest words.

f=open("kshitiz.txt","r")
x=f.read()
l=x.split()
maxi=max(l,key=len)
print(maxi)