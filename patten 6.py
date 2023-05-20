n = int(input("enter the number of rows"))
y = n - 1
sp = "  "
x = n
while (x > 0):
  print(sp * y + "  * " * x)
  x = x - 1
  y = y + 1
