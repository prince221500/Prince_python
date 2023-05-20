# Write a Python program to seprate  all words containg an alphabet A in the file 

f=open("old.txt","r")
l=f.readlines()
o=open("old.txt","w")
n=open("new.txt","w")
for i in l:
    if "A" in i :
        n.write(i)
    else:
        o.write(i)
    