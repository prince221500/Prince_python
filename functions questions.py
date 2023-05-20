print("********* fibonnachi serius using functions with no argumet no retun")
def kshitiz():
    x=int(input("enter the number of  the terrms "))
    if x==1:
        print("0")
    else:
        a=0
        b=1
        for i in range(2,x+1):
            c=a+b
            a=b
            b=c
            print(i.rjust(b))
kshitiz()

print("********* reverse of the number using functions with no argumet no retun")
def reverse():
    x=int(input("enter the number "))
    sum=0
    while x>0:
        rem=x%10
        sum=sum*10+rem
        x=x//10
    print(sum)
reverse()

print("********* number is neon or not using functions with no argumet with retun")
def neon():
    x=int(input("enter the number "))
    s=x*x
    sum=0
    while(s!=0):
        sum=sum+s%10
        s=s//10
    return(sum==x)
z=neon()
print(z)

print("********* fibonachi using functions with  argumet with no retun")
def vindhya(x):
    if x==1:
        print("0")
    else:
        a=0
        b=1
        for i in range(2,x+1):
            c=a+b
            a=b
            b=c
            print(b)
x=int(input("enter the number of  the terrms "))
vindhya(x)

#print("********* reverse using functions with  argumet with no retun")
#def reverse1():
 #   sum=0
  #  while x>0:
   #     rem=x%10
    #    sum=sum*10+rem
     #   x=x//10
    #print(sum)
#x=int(input("enter the number "))
#reverse1()

print("********* neon number using functions with  argumet with no retun")
def neon2(a):
    s=a*a
    sum=0
    while(s!=0):
        sum=sum+s%10
        s=s//10
    print(sum==a)
x=int(input("enter the number "))
neon2(x)

