# Write a Python program to read last n lines of a file.

f=open("kshitiz.txt","r")
x=f.read()
n=int(input("enter the number of line you want to read  "))
f.seek(0)
line=f.readlines()
last=line[-n:]
for i in last:
    print(i.strip())