print("************* NO ARGUMENT NO RETURN *******************")
def kshitiz():
      x=int(input("enter the  number"))
      y=int(input("enter the second number"))
      z=x+y
      print(z)
kshitiz()

print("************* NO ARGUMENT with RETURN *******************")
def shubh():
    x=int(input("enter the number  "))
    y=int(input("enter the number  "))
    return x+y
z=shubh()
print(z)

print("************* ARGUMENT NO RETUN *******************")
def radhika(a,b):
    z=a+b
    print(z)
x=int(input("enter the  number   "))
y=int(input("enter the number    "))
radhika(x,y)

print("************* ARGUMENT with RETUN *******************")
def vindhya(x,y):
    return x+y
x=int(input("enter any number "))
y=int(input("enter any number "))
z=vindhya(x,y)
print(z)