# map function can be used to take input in a single line or to map the two objects toghter 

# example of function retunig the square of each element of the list 
def vindhya(x):
    return x*x
ls=list(map(int,input("enter the list ").split())) #take list input

ls1=list(map(vindhya,ls))
print(*ls1)

# using the lambda function in with of the map function 

f=lambda a:a*a
ls=list(map(int,input("enter the list ").split()))
ls1=list(map(f,ls))
print(*ls1)
