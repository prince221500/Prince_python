d={}
x=int(input("enter the range"))
for i in range(x):
    k=eval(input("enter the key"))
    v=eval(input("enter the value"))
    d.update({k:v})
    print(d)
for i in range(x):
  print(v+i,end=" ")