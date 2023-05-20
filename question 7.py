print("enter the name of  the souc file : ")
s=input()
print("enter the name of  the target file : ")
t=input()
f=open(s,"r")
second=open(t,"r")
for i in f:
    second.write(i)
