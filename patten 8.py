n = int(input("enter the number of rows"))
x = 0
sp = " "
while (x < n):
  y = 2 * (n - x)
  print("*" * x + y * sp + "*" * x)
  x = x + 1
