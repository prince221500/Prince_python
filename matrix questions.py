print("hello  python ")
n=int(input("enter the number of the rows"))
v=int(input("enter the number of the col"))
ls=[]
for i in range(n):
    ls1=[]
    for j in range(v):
        a=int(input("enter the elments"))
        ls1.append(a)
    ls.append(ls1)
for i in range(n):
    for j in range(v):
        print(ls[i][j],end=" ")
    print()
print("***************** printing diagonal of the matrix *******************")

for i in range(n):
    for j in range(v):
        if(i==j):
            print(ls[i][j],end=" ")
        else:
            print( end=" ")
    print()

print("************* printing the antidiagonal of the matrix ****************")

for i  in range(n):
    for j  in range(v):
        if(i+j)==n-1:
            print(ls[i][j],end=" ")
        else:
            print(end=" ")
    print()

print("************* printing the boundary of the matrix *************")

for i in range(n):
    for j in range(v):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print(ls[i][j],end="  ")
        else:
            print(end="  ")
    print()

print("************* print the upper half of the matrix *************")

for i in range(n):
    for j in range(v):
        if (i+j)<=n-1:
            print(ls[i][j],end=" ")
    print()

print("************* print the lower half of the matrix *************")
for i in range(n):
    for j in range(v):
        if (i+j)>=n+1:
            print(ls[j][i],end=" ")
    print()

print("************* print the matrix in the zig zig form *************")

for i in range (n):
    if(i%2==0):
       for j in range(v):
        print(ls[i][j],end=" ")
    else:
        for j in range(v-1,-1,-1):
            print(ls[i][j],end=" ")
    print()

print("************* print the matrix diagonal in the zig zig form *************")


# n = 6
# A = [1,2,1,1,2,1]
# ps = [0]*(n+1)
# for i in range(1, n + 1):
#     ps[i] = ps[i - 1] + A[i - 1]
# print(ps)