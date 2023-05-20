# Write a Python program to write a list to a file

l=list(map(int,input().split()))
f=open("text.txt","w")
for i in l:
    f.write(str(i)+"\n")
f.close()

# f=open("text.txt","r")
# x=f.read()
# print(x)