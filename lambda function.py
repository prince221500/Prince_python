# sum of twwo number using lambda 
f=lambda x,y:x+y
x=int(input("enter the number 1  "))
y=int(input("enter the nyumber 2  "))
print("sum of two numbers is ",f(x,y))
print( )

# prininting the cube of the number
f=lambda x:x*x*x
x=int(input("enter the number "))
print("cube of the number is ",f(x))
print( )

# printing the gretest of two numbers using lambda 
f=lambda a,b : a if a>b else b 
x=int(input("enter the number 1  "))
y=int(input("enter the nyumber 2  "))
print("the grestest of two numbers among are  ",f(x,y))

print(f)