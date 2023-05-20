# Write a Python program to combine each line from first file with the 
# corresponding line in second file.

f1 = open("aaa.txt")
f2 = f1.readlines()
g1 = open("bbb.txt")
g2 = g1.readlines()
h1 = f2+g2
print(h1)