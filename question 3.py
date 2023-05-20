#  Write a Python program to read a file line by line store it into an array.

f=open("kshitiz.txt","r")
lines = []
for line in f:
        lines.append(line)

# Print the lines variable
print(*lines)
