# write a pyton progeram to count the number of line in the text file
f=open("kshitiz.txt","r")
x=f.read()
print(x)


f.seek(0)
y=f.readlines()     # readline retuns the list of the number
print(y) 
count=0
for i in y:
    count=count+1    ## for counting number of lines  in the python file
print(count)


k=x.split()           # splits split the list element an dstore in another list and then count the number of words
l=len(k)             # for counting the number of words in the text file
print(l)


# n=0
# for w in k:          # can also used to count the words in the text file 
#     n=n+1       
# print(n)


f.close()